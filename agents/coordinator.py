"""Coordinator agent that orchestrates diagnostics."""
from __future__ import annotations

from typing import Sequence

from autogen import AssistantAgent, GroupChat, GroupChatManager, token_count_utils
# Add the following imports if they exist in your framework:
from autogen.termination import MaxMessageTermination, TextMentionTermination

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
            system_message=(
                "You are the Coordinator agent, responsible for managing the entire diagnostic session. "
                "Your main tasks are:\n"
                "- Guide and facilitate communication between all specialist agents throughout the session.\n"
                "- Gather findings and responses from each specialist.\n"
                "- Continuously monitor progress and maintain focus on diagnosing the provided issue.\n"
                "- When a comprehensive diagnostic report is ready, clearly announce that the report is complete and explicitly terminate the discussion for all agents by saying "Terminate".\n"
                "Do not allow further conversation after the report is delivered. Be concise, organized, and authoritative in your coordination."
                ),
            llm_config=LLM_CONFIG,
        )
        self.last_token_count: int | None = None

    def run_diagnosis(self, issue: str, terminate_keyword: str = "TERMINATE") -> str:
        """Run a diagnostic session given an issue description.
        Terminates if the terminate_keyword is provided or if session count reaches 10.
        """
        participants = [self.agent] + [s.agent for s in self.specialists]
        
        # Setup termination conditions
        max_msg_termination = MaxMessageTermination(max_messages=10)
        text_termination = TextMentionTermination("Terminate")
        combined_termination = max_msg_termination | text_termination

        chat = GroupChat(
            participants=participants, messages=[{"role": "user", "content": issue}],
            termination_condition=combined_termination  # Pass to GroupChat if supported
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
