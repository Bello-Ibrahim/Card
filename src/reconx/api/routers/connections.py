"""Connection management, connection testing and query preview."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query

from reconx.api.deps import (
    ConnectionRepoDep,
    PrincipalDep,
    requires,
)
from reconx.api.schemas import (
    ConnectionRequest,
    ConnectionTestRequest,
    MessageResponse,
    QueryPreviewRequest,
    QueryPreviewResponse,
)
from reconx.common.errors import ReconXError
from reconx.common.logging import get_logger
from reconx.common.templating import render_deep
from reconx.config.connections import SECRET_FIELDS, ConnectionDefinition, ConnectionType
from reconx.config.enums import Permission, SourceType
from reconx.connectors import available_connectors, get_connector
from reconx.security.secrets import get_secret_resolver

log = get_logger(__name__)
router = APIRouter(prefix="/api/connections", tags=["connections"])

#: Connection type -> connector source type used for test/list operations.
_CONNECTOR_FOR: dict[str, SourceType] = {
    "s3": SourceType.S3,
    "storagegrid": SourceType.STORAGEGRID,
    "sftp": SourceType.SFTP,
    "jdbc": SourceType.JDBC,
    "kafka": SourceType.KAFKA,
    "filesystem": SourceType.FILESYSTEM,
}


def _resolved_config(connection: ConnectionDefinition, variables: dict[str, Any] | None = None) -> dict[str, Any]:
    resolver = get_secret_resolver()
    config = resolver.resolve_mapping(connection.config, SECRET_FIELDS)
    return render_deep(config, variables or {}, strict=False)


@router.get("", summary="List connections (secrets masked)")
def list_connections(
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_VIEW))],
    type: str | None = None,
    environment: str | None = None,
    enabled: bool | None = None,
) -> dict[str, Any]:
    items = [c.masked() for c in repository.list(conn_type=type, environment=environment, enabled=enabled)]
    return {"items": items, "total": len(items)}


@router.get("/types", summary="Supported connection and source types")
def connection_types(principal: PrincipalDep) -> dict[str, Any]:
    return {
        "connectionTypes": [t.value for t in ConnectionType],
        "connectors": available_connectors(),
    }


@router.post("", status_code=201, summary="Create a connection")
def create_connection(
    payload: ConnectionRequest,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_MANAGE))],
) -> dict[str, Any]:
    connection = ConnectionDefinition.model_validate(payload.connection)
    created = repository.create(connection, actor=principal.username)
    return {"connection": created.masked()}


@router.get("/{connection_id}", summary="Get a connection (secrets masked)")
def get_connection(
    connection_id: str,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_VIEW))],
) -> dict[str, Any]:
    return {"connection": repository.get(connection_id).masked()}


@router.put("/{connection_id}", summary="Update a connection")
def update_connection(
    connection_id: str,
    payload: ConnectionRequest,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_MANAGE))],
) -> dict[str, Any]:
    connection = ConnectionDefinition.model_validate({**payload.connection, "connectionId": connection_id})
    updated = repository.update(connection, actor=principal.username)
    return {"connection": updated.masked()}


@router.delete("/{connection_id}", summary="Delete a connection")
def delete_connection(
    connection_id: str,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_MANAGE))],
) -> MessageResponse:
    repository.delete(connection_id, actor=principal.username)
    return MessageResponse(message=f"Connection '{connection_id}' deleted")


@router.post("/{connection_id}/test", summary="Test a stored connection")
def test_connection(
    connection_id: str,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_TEST))],
) -> dict[str, Any]:
    connection = repository.get(connection_id)
    connector = get_connector(_CONNECTOR_FOR[str(connection.type)])
    config = _resolved_config(connection)
    problems = connector.validate(config)
    result = connector.test_connection(config)
    repository.record_test_result(
        connection_id, success=result.success, message=result.message, actor=principal.username
    )
    return {**result.to_dict(), "validationWarnings": problems}


@router.post("/test", summary="Test an unsaved connection")
def test_unsaved(
    payload: ConnectionTestRequest,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_TEST))],
) -> dict[str, Any]:
    if not payload.connection:
        raise HTTPException(status_code=400, detail="A connection payload is required")
    connection = ConnectionDefinition.model_validate(payload.connection)
    connector = get_connector(_CONNECTOR_FOR[str(connection.type)])
    config = _resolved_config(connection)
    problems = connector.validate(config)
    result = connector.test_connection(config)
    return {**result.to_dict(), "validationWarnings": problems}


@router.post(
    "/{connection_id}/preview",
    response_model=QueryPreviewResponse,
    summary="Preview a query or table (any SQL dialect, with ${variable} substitution)",
)
def preview(
    connection_id: str,
    payload: QueryPreviewRequest,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_TEST))],
) -> Any:
    """Execute a read-only statement and return the first rows.

    The statement is sent verbatim, so SQL Server ``SELECT TOP (n) ... WITH
    (NOLOCK)``, Oracle ``FETCH FIRST`` and PostgreSQL ``LIMIT`` all work.
    ``${variables}`` are substituted first - in the query *and* in the table
    name - which is exactly what the run will do.
    """
    connection = repository.get(connection_id)
    if str(connection.type) != "jdbc":
        raise HTTPException(
            status_code=400,
            detail=f"Query preview is only available for JDBC connections (this one is '{connection.type}')",
        )
    from reconx.connectors.jdbc import preview_query

    config = _resolved_config(connection, payload.variables)
    try:
        return preview_query(
            config,
            query=payload.query,
            table=payload.table,
            limit=payload.limit,
            variables=payload.variables,
        )
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc


@router.get("/{connection_id}/tables", summary="List tables and views on a JDBC connection")
def list_tables(
    connection_id: str,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_TEST))],
    schema: str | None = None,
    limit: int = Query(default=300, ge=1, le=5000),
) -> dict[str, Any]:
    connection = repository.get(connection_id)
    if str(connection.type) != "jdbc":
        raise HTTPException(status_code=400, detail="Table listing is only available for JDBC connections")
    from reconx.connectors.jdbc import list_tables as jdbc_list_tables

    try:
        return {"items": jdbc_list_tables(_resolved_config(connection), schema=schema, limit=limit)}
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc


@router.get("/{connection_id}/files", summary="List files/objects (S3, StorageGRID, SFTP, filesystem)")
def list_files(
    connection_id: str,
    repository: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.CONNECTION_TEST))],
    path: str = Query(default=""),
    pattern: str | None = None,
    limit: int = Query(default=200, ge=1, le=2000),
) -> dict[str, Any]:
    connection = repository.get(connection_id)
    connector = get_connector(_CONNECTOR_FOR[str(connection.type)])
    if not connector.supports_listing:
        raise HTTPException(
            status_code=400, detail=f"Connections of type '{connection.type}' cannot list files"
        )
    try:
        files = connector.list_files(_resolved_config(connection), path, pattern)
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc
    return {"items": [f.to_dict() for f in files[:limit]], "total": len(files)}
