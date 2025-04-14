from tools.find_civic_resource import register_tool as civic_tool
from mcp.server.fastmcp import FastMCP

# Build MCP object with tool name
mcp = FastMCP("CityStackAgentServer")

# Register tool
civic_tool(mcp)

# ✅ Export full FastAPI app (with MCP routes + health)
app = mcp.as_fastapi_app()

# Optional: root route
@app.get("/")
async def root():
    return {"status": "CityStack MCP server running"}

# Optional: local dev
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)
