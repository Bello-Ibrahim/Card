# JDBC drivers

Place vendor JDBC driver jars here before building the `scheduler` and `spark`
images. They are deliberately not committed: most are separately licensed and
every site pins its own version.

```bash
./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
```

That downloads PostgreSQL, MySQL, MariaDB, SQL Server and SQLite drivers from
Maven Central. **Oracle** (`ojdbc11.jar`) and **DB2** (`db2jcc4.jar`) must be
downloaded manually from the vendor because of their licence terms.
