"""Chainlit entrypoint for the diagnostic chatbot."""
from __future__ import annotations

import chainlit as cl

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


# Instantiate agents
_specialists = [
    EngineAgent(),
    TransmissionAgent(),
    BrakingAgent(),
    ElectricalAgent(),
    EmissionsAgent(),
]
_knowledge = KnowledgeAgent()
_repair = RepairProcedureAgent()
coordinator = CoordinatorAgent(_specialists, _knowledge, _repair)


@cl.on_chat_start
async def on_chat_start() -> None:
    """Send a greeting when the chat session starts."""
    await cl.Message(
        content="Welcome to the diagnostic chatbot! How can I assist you today?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message) -> None:
    """Handle incoming messages from the mechanic."""
    report, token_count = coordinator.run_diagnosis(message.content)
    await cl.Message(content=report).send()
    await cl.Message(content=f"Token count for session: {token_count}").send()

