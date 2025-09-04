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
                "You are a repair expert. When given a fault, respond with a clear, detailed, and concise repair procedure. "
                "Always include: a list of required parts, necessary tools, and step-by-step instructions for the repair. "
                "Format your response to be easy to follow, and highlight safety precautions where relevant. "
                "Avoid speculation—if you do not have a procedure for a given fault, state 'Procedure not found.'"
            ),
            llm_config=LLM_CONFIG,
        )

    def get_procedure(self, fault: str) -> str:
        """Return repair instructions for a given fault."""
        return self.procedures.get(fault, "Procedure not found.")
