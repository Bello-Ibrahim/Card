"""Reconciliation advisor endpoints (chat + recommendations)."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends

from reconx.advisor.recommender import suggest_match_logic
from reconx.api.deps import AdvisorDep, DatabaseDep, requires
from reconx.api.schemas import (
    AdvisorAnalyseRequest,
    AdvisorChatRequest,
    MatchLogicSuggestionRequest,
)
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import LogicalOperator, Permission
from reconx.config.store import Collections

log = get_logger(__name__)
router = APIRouter(prefix="/api/advisor", tags=["advisor"])


@router.post("/chat", summary="Ask the reconciliation advisor a question")
def chat(
    payload: AdvisorChatRequest,
    advisor: AdvisorDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    context = advisor.build_context(recon_id=payload.recon_id, run_id=payload.run_id)
    reply = advisor.answer(
        payload.question, context, history=payload.history, allow_llm=payload.allow_llm
    )
    return {
        **reply.to_dict(),
        "context": {
            "reconId": context.recon_id,
            "runId": context.run_id,
            "legCount": len(context.legs),
            "exceptionSample": len(context.exceptions),
            "hasProfiles": bool(context.profiles),
        },
    }


@router.post("/analyse", summary="All advisor findings for a reconciliation or run")
def analyse(
    payload: AdvisorAnalyseRequest,
    advisor: AdvisorDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    context = advisor.build_context(recon_id=payload.recon_id, run_id=payload.run_id)
    advice = advisor.advise(context)
    return {
        "reconId": context.recon_id,
        "runId": context.run_id,
        "generatedAt": utcnow().isoformat(),
        "advice": [item.to_dict() for item in advice],
        "counts": {
            severity: sum(1 for a in advice if a.severity.value == severity)
            for severity in ("CRITICAL", "WARNING", "SUGGESTION", "INFO")
        },
    }


@router.get("/profiles", summary="Stored column profiles (key and comparison candidates)")
def profiles(
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
    recon_id: str | None = None,
    run_id: str | None = None,
    limit: int = 5,
) -> dict[str, Any]:
    query: dict[str, Any] = {}
    if run_id:
        query["runId"] = run_id
    elif recon_id:
        query["reconId"] = recon_id
    items = list(
        db[Collections.COLUMN_PROFILES].find(query, {"_id": False}).sort("createdAt", -1).limit(limit)
    )
    return {"items": items, "count": len(items)}


@router.post("/suggest-match-logic", summary="Draft a multi-rule matching logic from profiled columns")
def suggest(
    payload: MatchLogicSuggestionRequest,
    advisor: AdvisorDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
) -> dict[str, Any]:
    context = advisor.build_context(recon_id=payload.recon_id, run_id=payload.run_id)
    if not context.profiles:
        return {
            "matchLogic": None,
            "reason": (
                "No column profile is available yet. Run the reconciliation with source profiling "
                "enabled (Analyse sources / --profile) and try again."
            ),
        }
    profile = context.profiles[0]
    key_columns = payload.key_columns or [
        candidate["leftColumn"] for candidate in profile.get("keyCandidates", [])[:2]
    ]
    logic = suggest_match_logic(
        profile, operator=LogicalOperator(payload.operator), key_columns=key_columns
    )
    return {
        "matchLogic": logic or None,
        "keyColumnsExcluded": key_columns,
        "legId": profile.get("legId"),
        "reason": (
            "Value-bearing columns and reference columns are placed in separate rules so you can switch "
            "the combination between AND (both must agree) and OR (either is enough)."
            if logic
            else "No comparable columns were found outside the key."
        ),
    }
