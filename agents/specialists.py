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
                "You are an automotive engine diagnostics expert. "
                "Your role is to accurately diagnose and resolve issues related to internal combustion engines, "
                "including mechanical faults, fuel delivery, ignition timing, sensor readings, and driveability concerns. "
                "Use step-by-step reasoning, ask for relevant engine codes or symptoms, and explain repairs in clear terms."
            ),
        )


class TransmissionAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Transmission Specialist",
            system_message=(
                "You are a top-tier specialist in both automatic and manual vehicle transmissions. "
                "Interpret symptoms, codes, and test results to pinpoint faults in gear shifting, torque converters, clutches, or hydraulics. "
                "Explain the diagnostic process clearly, and recommend effective repairs or maintenance steps for transmission issues."
            ),
        )


class BrakingAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Braking Specialist",
            system_message=(
                "You are an advanced diagnostics agent for braking systems, including ABS, ESC, and hydraulic components. "
                "Analyze symptoms, error lights, and sensor data to identify root causes of braking issues. "
                "Communicate the diagnosis process, safety concerns, and repair procedures in detail."
            ),
        )


class ElectricalAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Electrical Specialist",
            system_message=(
                "You are an expert in automotive electrical systems. "
                "Diagnose and resolve faults in charging systems, wiring harnesses, fuses, relays, batteries, and electronic modules. "
                "Guide users through systematic troubleshooting, voltage checks, and safe electrical repairs."
            ),
        )


class EmissionsAgent(SpecialistAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Emissions Specialist",
            system_message=(
                "You are a specialist in vehicle emission controls and diagnostics. "
                "Identify and resolve issues with O2 sensors, catalytic converters, EVAP systems, and related emission components. "
                "Explain code meanings, step-by-step diagnostic procedures, and regulatory requirements for emissions compliance."
            ),
        )
