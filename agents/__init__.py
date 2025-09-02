"""Agent package for vibeAutoGen diagnostic chatbot.

This module also centralizes configuration for the language model. The
project targets the Azure OpenAI API, so the :data:`LLM_CONFIG` defined
here reads the necessary connection details from environment variables.

Set the following variables before running the application:

```
AZURE_OPENAI_API_KEY      # service API key
AZURE_OPENAI_ENDPOINT     # e.g. https://my-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT   # name of the model deployment
AZURE_OPENAI_API_VERSION  # optional, defaults to 2023-07-01-preview
```

The resulting configuration dictionary is imported by all agents to ensure
they share the same model settings.
"""

from __future__ import annotations

import os
from dotenv import load_dotenv


# Load environment variables from a .env file if present
load_dotenv()


def _build_azure_config() -> dict:
    """Create an LLM config dictionary for Azure OpenAI."""

    return {
        "model": os.getenv("AZURE_OPENAI_DEPLOYMENT", ""),
        "api_key": os.getenv("AZURE_OPENAI_API_KEY", ""),
        "base_url": os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        "api_type": "azure",
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2023-07-01-preview"),
    }


# Shared configuration used by all agents
LLM_CONFIG: dict = {"config_list": [_build_azure_config()]}


__all__ = ["LLM_CONFIG"]

