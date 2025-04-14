import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def simulate():
    server_url = "http://localhost:8090/sse"

    async with sse_client(url=server_url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("🔗 Connected to CityStackAgent Server (SSE Mode)")
            print("Available tools: find_civic_resource")
            print("-" * 60)

            while True:
                tool = input("Enter tool name (or 'exit' to quit): ").strip()

                if tool == "exit":
                    break

                if tool == "find_civic_resource":
                    resource_type = input("🔎 Resource type (e.g., hospital): ").strip().lower()
                    result = await session.call_tool(tool, {"resource_type": resource_type})
                else:
                    print("❌ Unknown or disabled tool. Try again with: find_civic_resource")
                    continue

                print("✅ Tool Response:")
                for item in result.content:
                    print(item.text)
                print("-" * 60)

if __name__ == "__main__":
    asyncio.run(simulate())
