"""Repair procedure agent for providing step-by-step guides."""
from __future__ import annotations

from autogen import AssistantAgent

from . import LLM_CONFIG


class RepairProcedureAgent:
    """Provides repair instructions once a fault is confirmed."""

    def __init__(self, procedures: dict | None = None) -> None:
        self.procedures = procedures or {}
        self.agent = AssistantAgent(
            name="Manual Publisher",
            system_message=(
                "Provide parts lists, tool requirements and repair steps when given a fault."
            ),
            llm_config=LLM_CONFIG,
        )

    def get_procedure(self, fault: str) -> str:
        """Return repair instructions for a given fault."""
        return self.procedures.get(fault, "Procedure not found.")

