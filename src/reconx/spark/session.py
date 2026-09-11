"""SparkSession construction.

Resource sizing, AQE, shuffle behaviour and the Kubernetes settings are all
driven by configuration so the same job runs unchanged on ``local[*]``, a
standalone cluster and Spark-on-Kubernetes.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from reconx.common.logging import get_logger
from reconx.config.models import SparkOverrides
from reconx.config.settings import Settings, get_settings

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import SparkSession

log = get_logger(__name__)


def build_spark_conf(
    settings: Settings | None = None,
    overrides: SparkOverrides | None = None,
    *,
    app_name: str = "reconx",
) -> dict[str, str]:
    """Compose the full Spark configuration for a reconciliation run."""
    settings = settings or get_settings()
    spark_settings = settings.spark
    overrides = overrides or SparkOverrides()

    shuffle_partitions = overrides.shuffle_partitions or spark_settings.shuffle_partitions
    broadcast_mb = (
        overrides.broadcast_threshold_mb
        if overrides.broadcast_threshold_mb is not None
        else spark_settings.broadcast_threshold_mb
    )
    dynamic = (
        overrides.dynamic_allocation
        if overrides.dynamic_allocation is not None
        else spark_settings.dynamic_allocation
    )

    conf: dict[str, str] = {
        "spark.app.name": app_name,
        "spark.sql.shuffle.partitions": str(shuffle_partitions),
        "spark.sql.adaptive.enabled": str(spark_settings.adaptive_enabled).lower(),
        "spark.sql.adaptive.coalescePartitions.enabled": "true",
        "spark.sql.adaptive.skewJoin.enabled": "true",
        "spark.sql.adaptive.localShuffleReader.enabled": "true",
        "spark.sql.autoBroadcastJoinThreshold": str(int(broadcast_mb) * 1024 * 1024)
        if int(broadcast_mb) >= 0
        else "-1",
        "spark.sql.sources.partitionOverwriteMode": "dynamic",
        "spark.sql.parquet.compression.codec": "snappy",
        "spark.sql.legacy.timeParserPolicy": "CORRECTED",
        "spark.sql.session.timeZone": "UTC",
        "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
        "spark.kryoserializer.buffer.max": "512m",
        "spark.sql.execution.arrow.pyspark.enabled": "true",
        "spark.sql.execution.arrow.pyspark.fallback.enabled": "true",
        "spark.driver.cores": str(overrides.driver_cores or spark_settings.driver_cores),
        "spark.driver.memory": overrides.driver_memory or spark_settings.driver_memory,
        "spark.driver.maxResultSize": "2g",
        "spark.executor.cores": str(overrides.executor_cores or spark_settings.executor_cores),
        "spark.executor.memory": overrides.executor_memory or spark_settings.executor_memory,
        "spark.executor.instances": str(overrides.executor_instances or spark_settings.executor_instances),
        "spark.dynamicAllocation.enabled": str(dynamic).lower(),
        "spark.ui.showConsoleProgress": "false",
    }

    if dynamic:
        conf.update(
            {
                "spark.dynamicAllocation.minExecutors": str(spark_settings.dynamic_allocation_min_executors),
                "spark.dynamicAllocation.maxExecutors": str(spark_settings.dynamic_allocation_max_executors),
                "spark.dynamicAllocation.shuffleTracking.enabled": "true",
                "spark.dynamicAllocation.executorIdleTimeout": "120s",
            }
        )
    if spark_settings.event_log_dir:
        conf["spark.eventLog.enabled"] = "true"
        conf["spark.eventLog.dir"] = spark_settings.event_log_dir
    if spark_settings.local_dir:
        conf["spark.local.dir"] = spark_settings.local_dir
    if spark_settings.warehouse_dir:
        conf["spark.sql.warehouse.dir"] = spark_settings.warehouse_dir
    if spark_settings.extra_jars:
        conf["spark.jars"] = spark_settings.extra_jars
    if spark_settings.extra_packages:
        conf["spark.jars.packages"] = spark_settings.extra_packages

    if spark_settings.master.startswith("k8s://"):
        conf.update(
            {
                "spark.kubernetes.namespace": spark_settings.namespace,
                "spark.kubernetes.container.image": spark_settings.image,
                "spark.kubernetes.authenticate.driver.serviceAccountName": spark_settings.service_account,
                "spark.kubernetes.driver.podTemplateContainerName": "spark-kubernetes-driver",
                "spark.kubernetes.executor.deleteOnTermination": "true",
                "spark.kubernetes.submission.waitAppCompletion": "true",
                "spark.kubernetes.driver.label.app": "reconx-spark",
                "spark.kubernetes.executor.label.app": "reconx-spark",
            }
        )
    conf.update(overrides.extra_conf or {})
    return conf


def create_spark_session(
    app_name: str,
    *,
    settings: Settings | None = None,
    overrides: SparkOverrides | None = None,
    master: str | None = None,
    extra_conf: dict[str, str] | None = None,
) -> SparkSession:
    """Create (or reuse) a SparkSession configured for this platform."""
    from pyspark.sql import SparkSession

    settings = settings or get_settings()
    conf = build_spark_conf(settings, overrides, app_name=app_name)
    conf.update(extra_conf or {})

    builder = SparkSession.builder.appName(app_name)
    resolved_master = master or settings.spark.master
    if resolved_master:
        builder = builder.master(resolved_master)
    for key, value in conf.items():
        builder = builder.config(key, value)

    session = builder.getOrCreate()
    session.sparkContext.setLogLevel(os.getenv("SPARK_LOG_LEVEL", "WARN"))
    log.info(
        "spark.session_created",
        app_name=app_name,
        master=resolved_master,
        spark_application_id=session.sparkContext.applicationId,
        shuffle_partitions=conf.get("spark.sql.shuffle.partitions"),
        adaptive=conf.get("spark.sql.adaptive.enabled"),
    )
    return session


def stop_spark_session(session: SparkSession | None) -> None:
    if session is None:
        return
    try:
        session.stop()
    except Exception as exc:
        log.warning("spark.session_stop_failed", error=str(exc))


def spark_metrics(session: SparkSession) -> dict[str, Any]:
    """Lightweight execution metadata attached to run records."""
    context = session.sparkContext
    try:
        executors = context._jsc.sc().getExecutorMemoryStatus().size()
    except Exception:
        executors = None
    return {
        "sparkApplicationId": context.applicationId,
        "sparkVersion": context.version,
        "master": context.master,
        "defaultParallelism": context.defaultParallelism,
        "executorCount": executors,
        "webUrl": context.uiWebUrl,
    }
