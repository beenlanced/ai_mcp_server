"""
Simple example of how to build an easy Python Coded client to access tools 
from the MCP server using STREAMBLE_HTTP.py. Notice, no LLMs were involved

To run
- navigate to the directory where cleint_stdio.py exists
- At NEW terminal command line execute  `uv run client_streamable_http.py`


Make sure:
1. The server is running before running this script.
2. The server is configured to use streamable-http transport (i.e., set  transport = "streamable-http" in demo_server.py)
3. The server is listening on port 8050.

To run the server:
uv run demo_server.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    # Connect to the server using Streamable HTTP
    # Make sure to include `get_session_id` to avoid errors
    async with streamablehttp_client("http://localhost:8050/mcp") as (
        read_stream,
        write_stream,
        get_session_id
    ):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

             # Call our say_hello tool
            result = await session.call_tool("say_hello", arguments={"name": "Steve Rogers"})
            print(f"Greeting = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())