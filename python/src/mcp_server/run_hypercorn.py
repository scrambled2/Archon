"""Hypercorn runner for MCP server with HTTP/2 support."""
import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hypercorn.asyncio import serve
from hypercorn.config import Config
from src.mcp_server.mcp_server import mcp


def main():
    host = "0.0.0.0"
    port = int(os.getenv("ARCHON_MCP_PORT", "8051"))

    config = Config()
    config.bind = [f"{host}:{port}"]
    config.alpn_protocols = ["h2", "http/1.1"]
    config.accesslog = "-"
    config.errorlog = "-"
    config.loglevel = "INFO"

    print(f"Starting MCP server with Hypercorn (HTTP/2 enabled)")
    print(f"   URL: http://{host}:{port}/mcp")

    app = mcp.streamable_http_app()
    asyncio.run(serve(app, config))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("MCP server stopped")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
