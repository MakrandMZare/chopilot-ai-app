# Copilot Instructions for AI Agents

## Project Overview
This project is a starter template for building AI agents using LangGraph and CopilotKit, integrated with a Next.js frontend. The architecture is designed for rapid prototyping and extension of agent workflows, with clear separation between frontend (UI) and backend (agent logic).

## Key Components
- **Frontend (Next.js):** Located in `src/app/`. Main entry: `src/app/page.tsx`. UI actions and CopilotKit sidebar are customizable here.
- **Agent Backend (Python):** Main entry: `agent/agent.py`. Defines agent state, tools, workflow graph, and integration with LangGraph. Extend agent capabilities by adding tools via the `@tool` decorator.
- **Agent Server:** Managed via LangGraph CLI (`@langchain/langgraph-cli`). Configuration in `agent/langgraph.json`.
- **Integration:** Communication between frontend and agent is handled via CopilotKit and LangGraph APIs.

## Developer Workflows
- **Install dependencies:**
  - Node: `npm install` (root)
  - Python: `pip install -r agent/requirements.txt`
  - Agent setup: `npm run install:agent` (runs setup script for Python deps)
- **Start development servers:**
  - Both UI and agent: `npm run dev` (uses `concurrently`)
  - UI only: `npm run dev:ui`
  - Agent only: `npm run dev:agent`
- **Build production frontend:** `npm run build`
- **Lint code:** `npm run lint`

## Testing & CI
- **Smoke tests:** Defined in `.github/workflows/smoke.yml`. Runs on push, PR, and daily schedule. Matrix tests across OS, Node, and Python versions. Frontend startup is validated for all platforms.
- **Lock files:** Lock files are ignored in version control. Each developer should generate their own lock file locally.

## Patterns & Conventions
- **Agent tools:** Add new tools in `agent/agent.py` using the `@tool` decorator. Example:
  ```python
  @tool
def get_weather(location: str):
    return f"The weather for {location} is 70 degrees."
  ```
- **Agent state:** Extend `AgentState` in `agent/agent.py` for custom fields.
- **Workflow graph:** Use `StateGraph` to define agent workflow. Entry point is `chat_node`.
- **Environment variables:** Store secrets (e.g., OpenAI API key) in `agent/.env`.
- **Package managers:** Supports pnpm, npm, yarn, bun. Use your preferred tool, but do not commit lock files.

## External Dependencies
- **LangGraph** (`langgraph`, `langchain`, `langchain-openai`)
- **CopilotKit** (`@copilotkit/react-core`, etc.)
- **Next.js** (frontend)
- **OpenAI API** (agent model)

## Example Extension
To add a new agent tool:
1. Define the tool in `agent/agent.py` with `@tool`.
2. Add it to the `backend_tools` list.
3. Update agent state or workflow as needed.

## References
- Main agent logic: `agent/agent.py`
- Agent config: `agent/langgraph.json`
- Frontend: `src/app/page.tsx`
- CI: `.github/workflows/smoke.yml`
- Python deps: `agent/requirements.txt`
- Node deps: `package.json`

---
For unclear or missing conventions, please ask for clarification or review recent changes in the referenced files.