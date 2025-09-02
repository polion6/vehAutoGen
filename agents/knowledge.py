"""Knowledge and history agent for vehicle diagnostics."""
from __future__ import annotations

from autogen import AssistantAgent

from . import LLM_CONFIG


class KnowledgeAgent:
    """Manages access to the knowledge base and repair history."""

    def __init__(self, kb: dict | None = None) -> None:
        self.kb = kb or {}
        self.agent = AssistantAgent(
            name="Librarian",
            system_message="You manage diagnostic knowledge and repair histories.",
            llm_config=LLM_CONFIG,
        )

    def lookup(self, key: str) -> str:
        """Lookup information in the knowledge base."""
        return self.kb.get(key, "No data available.")

    def log(self, key: str, value: str) -> None:
        """Log a new entry in the knowledge base."""
        self.kb[key] = value

