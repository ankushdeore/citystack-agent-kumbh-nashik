from mcp.server.fastmcp import FastMCP
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
import uvicorn

from tools.find_civic_resource import register_tool as civic_tool

# 🔧 Create MCP server and register tool
mcp = FastMCP("CityStackAgent")
civic_tool(mcp)

# 🧠 Simple homepage (useful for humans and health checks)
async def homepage(request: Request) -> HTMLResponse:
    return HTMLResponse("""
    <html>
      <head><title>CityStack MCP Server</title></head>
      <body>
        <h1>✅ CityStack Agent for Kumbh Nashik 2027</h1>
        <p>This server is running and MCP-ready.</p>
      </body>
    </html>
    """)

from starlette.responses import PlainTextResponse  # ✅ Add this at the top with your other imports

def create_starlette_app(mcp_server: Server) -> Starlette:
    sse = SseServerTransport("/messages/")

    async def handle_sse(request: Request) -> None:
        async with sse.connect_sse(
            request.scope,
            request.receive,
            request._send
        ) as (read_stream, write_stream):
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options()
            )

    return Starlette(
        debug=False,
        routes=[
            Route("/", homepage),
            Route("/sse", handle_sse),
            Route("/mcp-verification.txt", lambda request: PlainTextResponse("y2CL3jYxR9FIrtS0ER62Srru8AH3rOBmdnVWRKJfh6U")),  # ✅ Add this line
            Mount("/messages/", app=sse.handle_post_message)
        ]
    )


# ✅ Expose ASGI app for Render or any MCP host
app = create_starlette_app(mcp._mcp_server)

# 🧪 Local testing (optional)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
