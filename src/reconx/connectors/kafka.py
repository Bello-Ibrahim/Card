"""Kafka connector.

Batch reads use Spark's ``kafka`` source with explicit start/end offsets so a
reconciliation over a bounded window is reproducible.  The same configuration
object works for streaming (``readStream``) which is why ``read_stream`` is
provided - the reconciliation engine consumes a DataFrame either way.

Payload decoding supports JSON (schema inferred or explicit), CSV-style
delimited values and raw strings.  Avro is decoded via
``from_avro`` when the spark-avro package is on the classpath, and the
connector reports a clear error when it is not, rather than failing obscurely
inside Spark.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConnectionFailedError, ConnectorError
from reconx.common.logging import get_logger
from reconx.config.enums import SourceType
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    OutputContext,
    SourceContext,
    register_connector,
)

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)

METADATA_COLUMNS = ("topic", "partition", "offset", "timestamp", "timestampType")


def spark_kafka_options(config: dict[str, Any]) -> dict[str, str]:
    """Translate a connection definition into Spark Kafka source options."""
    options: dict[str, str] = {
        "kafka.bootstrap.servers": str(config.get("bootstrapServers", "")),
        "kafka.security.protocol": str(config.get("securityProtocol", "PLAINTEXT")),
    }
    if config.get("saslMechanism"):
        options["kafka.sasl.mechanism"] = str(config["saslMechanism"])
        username = config.get("saslUsername", "")
        password = config.get("saslPassword", "")
        mechanism = str(config["saslMechanism"]).upper()
        login_module = (
            "org.apache.kafka.common.security.scram.ScramLoginModule"
            if mechanism.startswith("SCRAM")
            else "org.apache.kafka.common.security.plain.PlainLoginModule"
        )
        options["kafka.sasl.jaas.config"] = (
            f'{login_module} required username="{username}" password="{password}";'
        )
    if config.get("sslCaLocation"):
        options["kafka.ssl.truststore.location"] = str(config["sslCaLocation"])
    if config.get("sslCertificateLocation"):
        options["kafka.ssl.keystore.location"] = str(config["sslCertificateLocation"])
    if config.get("sslKeyPassword"):
        options["kafka.ssl.key.password"] = str(config["sslKeyPassword"])
    if not config.get("sslVerify", True):
        options["kafka.ssl.endpoint.identification.algorithm"] = ""
    for key, value in (config.get("extraProperties") or {}).items():
        options[key if key.startswith("kafka.") else f"kafka.{key}"] = str(value)
    return options


def confluent_config(config: dict[str, Any], group_id: str | None = None) -> dict[str, Any]:
    """Configuration for the confluent-kafka admin/consumer client."""
    conf: dict[str, Any] = {
        "bootstrap.servers": config.get("bootstrapServers", ""),
        "security.protocol": config.get("securityProtocol", "PLAINTEXT"),
        "socket.timeout.ms": 10_000,
    }
    if group_id:
        conf["group.id"] = group_id
        conf["enable.auto.commit"] = False
        conf["auto.offset.reset"] = "earliest"
    if config.get("saslMechanism"):
        conf["sasl.mechanism"] = config["saslMechanism"]
        conf["sasl.username"] = config.get("saslUsername", "")
        conf["sasl.password"] = config.get("saslPassword", "")
    if config.get("sslCaLocation"):
        conf["ssl.ca.location"] = config["sslCaLocation"]
    if not config.get("sslVerify", True):
        conf["enable.ssl.certificate.verification"] = False
    for key, value in (config.get("extraProperties") or {}).items():
        conf[key] = value
    return conf


@register_connector
class KafkaConnector(DataSourceConnector):
    source_types = (SourceType.KAFKA,)
    display_name = "Apache Kafka"

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        return self._load(config, spark, streaming=False)

    def read_stream(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        """Structured-streaming variant - same configuration, unbounded source."""
        return self._load(config, spark, streaming=True)

    def _load(self, config: SourceContext, spark: SparkSession, *, streaming: bool) -> DataFrame:
        source = config.source
        options = spark_kafka_options(config.resolved_config)
        options["subscribe"] = source.topic or ""
        options["startingOffsets"] = str(source.options.get("startingOffsets", "earliest"))
        if not streaming:
            options["endingOffsets"] = str(source.options.get("endingOffsets", "latest"))
        if source.options.get("maxOffsetsPerTrigger"):
            options["maxOffsetsPerTrigger"] = str(source.options["maxOffsetsPerTrigger"])
        options["failOnDataLoss"] = str(source.options.get("failOnDataLoss", "false")).lower()
        group_prefix = config.conn("consumerGroupPrefix", "reconx")
        options["kafka.group.id"] = str(source.options.get("consumerGroup") or f"{group_prefix}-{source.id}")

        reader = spark.readStream if streaming else spark.read
        raw = reader.format("kafka").options(**options).load()
        log.info(
            "kafka.read",
            topic=source.topic,
            streaming=streaming,
            starting=options["startingOffsets"],
        )
        return self._decode(raw, config, spark)

    def _decode(self, raw: DataFrame, config: SourceContext, spark: SparkSession) -> DataFrame:
        from pyspark.sql import functions as F

        source = config.source
        message_format = str(source.options.get("messageFormat", source.format or "json")).lower()
        include_metadata = bool(source.options.get("includeMetadata", False))
        value_column = F.col("value").cast("string").alias("value")
        key_column = F.col("key").cast("string").alias("__kafka_key")

        if message_format == "json":
            schema = None
            if source.schema_spec and source.schema_spec.mode.value in ("explicit", "validate"):
                from reconx.spark.schema import build_struct_type

                schema = build_struct_type(source.schema_spec)
            if schema is None:
                json_strings = raw.select(value_column)
                sample = json_strings.limit(int(source.options.get("schemaSampleSize", 1000)))
                schema = spark.read.json(sample.select("value").rdd.map(lambda r: r.value)).schema
            decoded = raw.select(
                key_column,
                F.from_json(F.col("value").cast("string"), schema).alias("__payload"),
                *[F.col(c) for c in METADATA_COLUMNS],
            ).select("__kafka_key", "__payload.*", *METADATA_COLUMNS)
        elif message_format in ("csv", "delimited"):
            delimiter = str(source.options.get("delimiter", ","))
            columns = [c.strip() for c in str(source.options.get("columns", "")).split(",") if c.strip()]
            if not columns:
                raise ConnectorError(
                    f"source '{source.id}': CSV Kafka payloads require an 'columns' option listing field names"
                )
            split_column = F.split(F.col("value").cast("string"), delimiter)
            decoded = raw.select(
                key_column,
                *[split_column.getItem(i).alias(name) for i, name in enumerate(columns)],
                *[F.col(c) for c in METADATA_COLUMNS],
            )
        elif message_format == "avro":
            try:
                from pyspark.sql.avro.functions import from_avro
            except ImportError as exc:  # pragma: no cover - classpath dependent
                raise ConnectorError(
                    "Avro payloads require the spark-avro package on the Spark classpath "
                    "(spark.jars.packages=org.apache.spark:spark-avro_2.12:<spark-version>)"
                ) from exc
            avro_schema = source.options.get("avroSchema")
            if not avro_schema:
                raise ConnectorError(
                    f"source '{source.id}': Avro payloads require an 'avroSchema' option (JSON schema string)"
                )
            decoded = raw.select(
                key_column,
                from_avro(F.col("value"), str(avro_schema)).alias("__payload"),
                *[F.col(c) for c in METADATA_COLUMNS],
            ).select("__kafka_key", "__payload.*", *METADATA_COLUMNS)
        else:  # raw string payloads
            decoded = raw.select(key_column, value_column, *[F.col(c) for c in METADATA_COLUMNS])

        if not include_metadata:
            decoded = decoded.drop(*METADATA_COLUMNS)
        return decoded

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        from pyspark.sql import functions as F

        output = config.output
        options = spark_kafka_options(config.resolved_config)
        options["topic"] = output.topic or ""
        key_column = config.option("keyColumn")
        columns = list(dataframe.columns)
        payload = dataframe.select(
            (F.col(key_column).cast("string") if key_column else F.lit(None).cast("string")).alias("key"),
            F.to_json(F.struct(*[F.col(c) for c in columns])).alias("value"),
        )
        payload.write.format("kafka").options(**options).save()
        log.info("kafka.write", topic=output.topic)
        return {"target": output.topic, "type": "kafka"}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        try:
            from confluent_kafka.admin import AdminClient
        except ImportError:
            return ConnectionTestResult(
                False, "confluent-kafka is not installed - install reconx[connectors] to test Kafka"
            )
        try:
            admin = AdminClient(confluent_config(config))
            metadata = admin.list_topics(timeout=10)
            topics = sorted(metadata.topics.keys())
            return ConnectionTestResult(
                True,
                f"Connected to Kafka - {len(topics)} topic(s), {len(metadata.brokers)} broker(s)",
                latency_ms=int((time.time() - started) * 1000),
                details={"topics": topics[:25], "brokers": len(metadata.brokers)},
            )
        except Exception as exc:
            return ConnectionTestResult(
                False,
                f"Kafka connection failed: {type(exc).__name__}: {exc}",
                latency_ms=int((time.time() - started) * 1000),
            )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems = self._require(config, "bootstrapServers")
        protocol = str(config.get("securityProtocol", "PLAINTEXT"))
        if protocol.startswith("SASL"):
            if not config.get("saslMechanism"):
                problems.append("'saslMechanism' is required for SASL security protocols")
            if not config.get("saslUsername"):
                problems.append("'saslUsername' is required for SASL security protocols")
        return problems

    def message_count(
        self, config: dict[str, Any], topic: str, *, since_ms: int | None = None
    ) -> dict[str, Any]:
        """Offset-based availability probe used by the ``kafka_available`` condition."""
        try:
            from confluent_kafka import Consumer, TopicPartition
        except ImportError as exc:
            raise ConnectorError("confluent-kafka is required for Kafka availability conditions") from exc

        consumer = Consumer(confluent_config(config, group_id=f"reconx-probe-{int(time.time())}"))
        try:
            metadata = consumer.list_topics(topic, timeout=10)
            if topic not in metadata.topics or metadata.topics[topic].error:
                raise ConnectionFailedError(f"Kafka topic '{topic}' does not exist")
            partitions = list(metadata.topics[topic].partitions.keys())
            total = 0
            per_partition: dict[int, dict[str, int]] = {}
            for partition in partitions:
                tp = TopicPartition(topic, partition)
                low, high = consumer.get_watermark_offsets(tp, timeout=10, cached=False)
                start = low
                if since_ms is not None:
                    tp_time = TopicPartition(topic, partition, since_ms)
                    offsets = consumer.offsets_for_times([tp_time], timeout=10)
                    if offsets and offsets[0].offset >= 0:
                        start = offsets[0].offset
                    else:
                        start = high
                count = max(0, high - start)
                total += count
                per_partition[partition] = {"low": low, "high": high, "from": start, "available": count}
            return {"topic": topic, "totalMessages": total, "partitions": per_partition}
        finally:
            consumer.close()
