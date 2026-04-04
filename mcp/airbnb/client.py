import asyncio
import traceback

from mcp.client.stdio import stdio_client

from mcp import ClientSession, StdioServerParameters

server_parameters = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
)

async def main():
    # Connect to the MCP server using stdio and create a client session
    try:
        async with stdio_client(server_parameters) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                print("Available tools:", tools)

                # print("Calling tool...")

                location = "New York"
                result = await session.call_tool("airbnb_search", arguments={"location": location})

                print(f"Search result for {location}: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
