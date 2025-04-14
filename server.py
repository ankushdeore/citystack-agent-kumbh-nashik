from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CityStackAgentServer")

# Import and register tools
from tools.find_civic_resource import register_tool as civic_tool
civic_tool(mcp)

# ✅ Define this at the top level so Render can find it
app = mcp.sse_app()  # ASGI-compatible

# Optional: for local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)
# Add health endpoint
@app.get("/")
async def root():
    return {"status": "CityStack MCP server running"}