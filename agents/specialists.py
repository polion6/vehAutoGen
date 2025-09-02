"""Domain specialist agents for vehicle diagnostics."""
from __future__ import annotations

from autogen import AssistantAgent

from . import LLM_CONFIG


class SpecialistAgent:
    """Base class for domain specific specialist agents."""

    def __init__(self, name: str, system_message: str) -> None:
        self.agent = AssistantAgent(
            name=name, system_message=system_message, llm_config=LLM_CONFIG
        )


class EngineAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Engine Specialist",
            system_message=(
                "Expert in engine mechanics, fuel and ignition systems."
            ),
        )


class TransmissionAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Transmission Specialist",
            system_message=(
                "Expert in automatic and manual transmission diagnostics."
            ),
        )


class BrakingAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Braking Specialist",
            system_message=(
                "Expert in ABS, ESC and hydraulic braking systems."
            ),
        )


class ElectricalAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Electrical Specialist",
            system_message=(
                "Expert in charging systems, wiring and electrical faults."
            ),
        )


class EmissionsAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Emissions Specialist",
            system_message=(
                "Expert in emission controls, O2 sensors and EVAP systems."
            ),
        )

