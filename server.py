from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CityStackAgentServer")

# Import and register tools

from tools.find_civic_resource import register_tool as civic_tool

civic_tool(mcp)


# Run with SSE server directly (no keyword "sse")
if __name__ == "__main__":
    import uvicorn

    app = mcp.sse_app()  # ✅ Returns an ASGI-compatible app

    uvicorn.run(app, host="127.0.0.1", port=8090)
