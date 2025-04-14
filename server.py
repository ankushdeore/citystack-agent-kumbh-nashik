from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from tools.find_civic_resource import register_tool as civic_tool

# Create FastAPI app
app = FastAPI()

# Attach MCP to FastAPI
mcp = FastMCP("CityStackAgent", app=app)

# Register tool
civic_tool(mcp)

# ✅ Root health check
@app.get("/")
async def root():
    return {"status": "CityStack MCP server running"}

# ✅ For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)
