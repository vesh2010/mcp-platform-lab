from fastapi import FastAPI
import os
import socket

app = FastAPI(
    title="MCP Platform Lab",
    version=os.getenv("APP_VERSION", "0.1.0"),
)

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {
        "application": "mcp-platform",
        "version": APP_VERSION,
    }


@app.get("/info")
def info():
    return {
        "application": "mcp-platform",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
    }


@app.get("/tools")
def tools():
    return {
        "tools": [
            {
                "name": "get_platform_info",
                "description": "Returns runtime information about the platform.",
            }
        ]
    }


@app.get("/tools/get_platform_info")
def get_platform_info():
    return info()
