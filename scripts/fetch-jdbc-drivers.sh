#!/usr/bin/env bash
# Download the JDBC drivers ReconX needs on the Spark classpath.
#
# Spark reads and writes relational sources through the vendor's JDBC driver,
# which is deliberately NOT bundled: most are separately licensed, and every
# site pins its own version. Run this once (or bake the jars into the Spark
# image) and point SPARK_EXTRA_JARS at the directory.
#
#   ./scripts/fetch-jdbc-drivers.sh [target-dir]
#   export SPARK_EXTRA_JARS="$(ls -d $PWD/.jars/*.jar | paste -sd,)"
set -euo pipefail

TARGET="${1:-$(dirname "$0")/../.jars}"
MAVEN="${MAVEN_REPOSITORY:-https://repo1.maven.org/maven2}"
mkdir -p "$TARGET"

# groupId:artifactId:version  (Oracle and DB2 need a manual download - see docs)
DRIVERS=(
  "org/postgresql/postgresql/42.7.4/postgresql-42.7.4.jar"
  "org/xerial/sqlite-jdbc/3.46.1.3/sqlite-jdbc-3.46.1.3.jar"
  "com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar"
  "com/microsoft/sqlserver/mssql-jdbc/12.8.1.jre11/mssql-jdbc-12.8.1.jre11.jar"
  "org/mariadb/jdbc/mariadb-java-client/3.4.1/mariadb-java-client-3.4.1.jar"
)

for path in "${DRIVERS[@]}"; do
  filename="$(basename "$path")"
  if [[ -f "$TARGET/$filename" ]]; then
    echo "already present: $filename"
    continue
  fi
  echo "downloading: $filename"
  curl -fsSL "$MAVEN/$path" -o "$TARGET/$filename" || echo "  WARNING: could not download $filename"
done

echo
echo "Drivers in $TARGET:"
ls -1 "$TARGET"
echo
echo "Use them with:"
echo "  export SPARK_EXTRA_JARS=\"\$(ls -d \"$TARGET\"/*.jar | paste -sd,)\""
echo
echo "Oracle (ojdbc11.jar) and DB2 (db2jcc4.jar) require a manual download from the"
echo "vendor because of their licence terms - see docs/CONNECTORS.md."
