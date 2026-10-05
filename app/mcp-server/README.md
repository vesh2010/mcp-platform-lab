# MCP Server

The first application workload for the MCP Platform Lab.

## Endpoints

| Endpoint | Purpose |
|---|---|
| `/health` | Health check |
| `/version` | Application version |
| `/info` | Runtime information |
| `/tools` | Lists available tools |
| `/tools/get_platform_info` | Executes the first platform tool |

## Run locally

```bash
cd app/mcp-server
python -m venv .venv
# Activate the virtual environment for your OS
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8080
```

Open:

```text
http://localhost:8080/docs
```

## Why FastAPI?

**FastAPI** is intentionally used only as a lightweight HTTP application framework. Kubernetes is the focus of this project, not application-framework development.
