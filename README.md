# vehAutoGen

Diagnostic chatbot project built with [AutoGen](https://github.com/microsoft/autogen) and [Chainlit](https://github.com/Chainlit/chainlit).

The system defines a set of agents to assist mechanics in vehicle troubleshooting:

- **Coordinator Agent** – orchestrates the diagnostic workflow.
- **Specialist Agents** – domain experts for engine, transmission, braking, electrical and emissions systems.
- **Knowledge Agent** – manages diagnostic knowledge and repair history.
- **Repair Procedure Agent** – supplies step‑by‑step repair instructions.

## Azure OpenAI Configuration

The agents use the Azure OpenAI API. Copy ``.env.example`` to ``.env`` and
fill in your service details:

```bash
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=<deployment-name>
AZURE_OPENAI_API_VERSION=2023-07-01-preview  # optional
```

The ``.env`` file is loaded automatically when the application starts.

## Run the Chainlit app:

```bash
pip install -r requirements.txt
chainlit run app.py
```

