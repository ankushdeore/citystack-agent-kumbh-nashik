from mcp.server.fastmcp import FastMCP
from tools.find_civic_resource import register_tool as civic_tool

mcp = FastMCP("CityStackAgentServer")
civic_tool(mcp)

# ✅ Define ASGI app
app = mcp.sse_app()

# ✅ Health check endpoint — must be BEFORE __main__
@app.get("/")
async def root():
    return {"status": "CityStack MCP server running"}

# Optional: run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)
