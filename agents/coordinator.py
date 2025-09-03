"""Coordinator agent that orchestrates diagnostics."""
from __future__ import annotations

from typing import Sequence

from autogen import AssistantAgent, GroupChat, GroupChatManager, token_count_utils

from . import LLM_CONFIG

from .specialists import SpecialistAgent
from .knowledge import KnowledgeAgent
from .repair_procedure import RepairProcedureAgent


class CoordinatorAgent:
    """Central orchestrator managing specialist agents."""

    def __init__(
        self,
        specialists: Sequence[SpecialistAgent],
        knowledge_agent: KnowledgeAgent,
        repair_agent: RepairProcedureAgent,
    ) -> None:
        self.specialists = specialists
        self.knowledge_agent = knowledge_agent
        self.repair_agent = repair_agent
        self.agent = AssistantAgent(
            name="Coordinator",
            system_message="Manage the diagnostic session and compile reports.",
            llm_config=LLM_CONFIG,
        )
        self.last_token_count: int | None = None

    def run_diagnosis(self, issue: str) -> str:
        """Run a diagnostic session given an issue description."""
        participants = [self.agent] + [s.agent for s in self.specialists]
        chat = GroupChat(
            participants=participants, messages=[{"role": "user", "content": issue}]
        )
        manager = GroupChatManager(groupchat=chat, llm_config=LLM_CONFIG)
        manager.run()
        model = (
            self.agent.llm_config.get("config_list", [{}])[0].get(
                "model", "gpt-3.5-turbo-0613"
            )
        )
        self.last_token_count = token_count_utils.count_token(chat.messages, model=model)
        print(f"Token count for session: {self.last_token_count}")
        return chat.messages[-1]["content"]

