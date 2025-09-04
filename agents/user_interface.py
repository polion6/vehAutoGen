"""User interface agent connecting with the mechanic via Chainlit."""
from __future__ import annotations

import chainlit as cl
from autogen import UserProxyAgent


class UserInterfaceAgent(UserProxyAgent):
    """Handles interaction with the human mechanic."""

    def __init__(self) -> None:
        super().__init__(
            name="Service Advisor",
            human_input_mode="ALWAYS",  # Allow user input
        )

    async def get_car_info(self) -> dict[str, str]:
        """Prompt the user for car make, model, and issue/symptom."""
        make_response = await cl.AskUserMessage(
            content="Please enter your car's make:"
        ).send()
        make = make_response["content"] if make_response else ""

        model_response = await cl.AskUserMessage(
            content="Please enter your car's model:"
        ).send()
        model = model_response["content"] if model_response else ""

        issue_response = await cl.AskUserMessage(
            content="Please describe the issue or symptom:"
        ).send()
        issue = issue_response["content"] if issue_response else ""

        return {"make": make, "model": model, "issue": issue}
