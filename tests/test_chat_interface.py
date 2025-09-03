import os
import sys
from pathlib import Path
from unittest.mock import patch

# Ensure agent modules pick up valid environment configuration
os.environ.setdefault("AZURE_OPENAI_DEPLOYMENT", "dummy-model")
os.environ.setdefault("AZURE_OPENAI_API_KEY", "dummy-key")
os.environ.setdefault("AZURE_OPENAI_ENDPOINT", "https://example.com")
os.environ.setdefault("AZURE_OPENAI_API_VERSION", "2023-07-01-preview")

sys.path.append(str(Path(__file__).resolve().parents[1]))

from agents.coordinator import CoordinatorAgent
from agents.specialists import (
    EngineAgent,
    TransmissionAgent,
    BrakingAgent,
    ElectricalAgent,
    EmissionsAgent,
)
from agents.knowledge import KnowledgeAgent
from agents.repair_procedure import RepairProcedureAgent


def test_chat_interface_responds() -> None:
    """Ensure the coordinator produces a response for a given issue."""
    specialists = [
        EngineAgent(),
        TransmissionAgent(),
        BrakingAgent(),
        ElectricalAgent(),
        EmissionsAgent(),
    ]
    coordinator = CoordinatorAgent(specialists, KnowledgeAgent(), RepairProcedureAgent())
    issue = "there is a knocking sound in my toyota camry. How to i fix it?"

    class DummyChat:
        def __init__(self, participants, messages):
            self.participants = participants
            self.messages = messages

    class DummyManager:
        def __init__(self, groupchat, llm_config):
            self.groupchat = groupchat
            self.llm_config = llm_config

        def run(self):
            self.groupchat.messages.append({"role": "assistant", "content": "Mocked response"})

    with patch("agents.coordinator.GroupChat", DummyChat), \
         patch("agents.coordinator.GroupChatManager", DummyManager), \
         patch("agents.coordinator.token_count_utils.count_token", return_value=0):
        result = coordinator.run_diagnosis(issue)

    assert "Mocked response" in result
