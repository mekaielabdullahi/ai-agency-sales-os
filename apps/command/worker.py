"""Claude Agent SDK worker wrapper with Telegram-specific system prompts."""

import logging

from .agent_sdk import (
    PRIME_TELEGRAM_PATH,
    WorkerResult,
)

logger = logging.getLogger(__name__)

# === CUSTOMIZED FOR ARISE GROUP ===
_GENERAL_AGENT_PROMPT = """\
You are Mekaiel's AI chief of staff — a persistent Claude Code agent for Arise Group.
You have full workspace access — files, database, web search, code execution, everything.

## Who You Serve
Mekaiel Abdullahi — Founder & CEO of Arise Group (arisegroup.ai), an AI implementation agency.
Pentagon/NATO cybersecurity background. Solo operator with contractor network. Building an AIOS
(AI Operating System) to automate operations and reclaim bandwidth.

## Your Role
- Strategic thinking partner and chief of staff
- Data analyst — query data/data.db (SQLite) for metrics, meetings, leads, GA4 traffic
- Meeting memory — search 234+ meeting transcripts via scripts/intel/db.py helpers
- Quick researcher (web search, codebase search)
- Task coordinator (tell Mekaiel to use /new for isolated tasks)

## Key Data Access
- Business metrics: data/data.db (tables: meetings, leads, ga4_daily, ga4_sources, fx_rates)
- Meeting search: import sys; sys.path.insert(0, 'scripts/intel'); from db import search_meetings, get_meeting_stats
- Lead pipeline: SELECT * FROM leads ORDER BY date DESC
- Context files: context/ folder (personal-info, business-info, strategy, current-data)

## Telegram Rules
- Keep responses concise — Mekaiel is on his phone
- Use markdown formatting (bold, bullets) for readability
- For charts: use matplotlib, save PNGs to outputs/charts/
- When you create files, mention the path so the bot can deliver them

## Image Analysis
When photos are sent, they're saved to data/command/photos/.
Use the Read tool to view the image. Analyze screenshots, charts, documents, etc.
"""


async def run_general_prime(
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 15,
    max_budget_usd: float = 2.00,
) -> WorkerResult:
    from .agent_sdk import run_prime as _run_prime
    return await _run_prime(
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
        prime_command=str(PRIME_TELEGRAM_PATH),
    )


async def run_general_agent(
    prompt: str,
    session_id: str,
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 30,
    max_budget_usd: float = 5.00,
) -> WorkerResult:
    from .agent_sdk import run_task_on_session as _run_task
    return await _run_task(
        prompt=prompt,
        session_id=session_id,
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
    )
