from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from tools.find_civic_resource import register_tool as civic_tool

# Create FastAPI app
app = FastAPI()

# Connect MCP to FastAPI app
mcp = FastMCP("CityStackAgentServer", app=app)
civic_tool(mcp)

# ✅ MCP-compatible root route (for registry)
@app.get("/")
async def root():
    return {"status": "CityStack MCP server running"}

# ✅ Optional: for local dev
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)
