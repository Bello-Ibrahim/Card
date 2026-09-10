"""Data source connectors.

Adding a new source type means dropping a module in this package that
subclasses :class:`~reconx.connectors.base.DataSourceConnector` and decorating
it with :func:`~reconx.connectors.base.register_connector`.  The reconciliation
engine is never modified.
"""

from reconx.connectors.base import (  # noqa: F401
    ConnectionTestResult,
    DataSourceConnector,
    FileInfo,
    OutputContext,
    SourceContext,
    available_connectors,
    get_connector,
    register_connector,
)


def _load_builtin_connectors() -> None:
    """Import built-in connector modules so they self-register."""
    from importlib import import_module

    for module in (
        "filesystem",
        "s3",
        "storagegrid",
        "sftp",
        "jdbc",
        "kafka",
        "excel",
        "temp_view",
    ):
        import_module(f"reconx.connectors.{module}")


_load_builtin_connectors()
