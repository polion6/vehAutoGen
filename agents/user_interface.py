"""User interface agent connecting with the mechanic via Chainlit."""
from __future__ import annotations

from autogen import UserProxyAgent


class UserInterfaceAgent(UserProxyAgent):
    """Handles interaction with the human mechanic."""

    def __init__(self) -> None:
        super().__init__(
            name="Service Advisor",
            human_input_mode="ALWAYS",  # Allow user input
        )

    def get_car_info(self):
        """Prompt the user for car make, model, and issue/symptom."""
        make = input("Please enter your car's make: ")
        model = input("Please enter your car's model: ")
        issue = input("Please describe the issue or symptom: ")
        return {
            "make": make,
            "model": model,
            "issue": issue
        }
