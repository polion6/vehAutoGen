"""User interface agent connecting with the mechanic via Chainlit."""
from __future__ import annotations

from autogen import UserProxyAgent


class UserInterfaceAgent(UserProxyAgent):
    """Handles interaction with the human mechanic."""

    def __init__(self) -> None:
        super().__init__(
            name="Service Advisor",
            human_input_mode="NEVER",
        )

