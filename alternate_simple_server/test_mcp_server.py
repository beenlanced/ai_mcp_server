import asyncio
from fastmcp import Client

client = Client("simple_calc_server.py")

async def call_tool(a: float, b: float) -> str:
    async with client:
        result = await client.call_tool("divide", {"a": a, "b": b})
        print(result)

asyncio.run(call_tool(10.0, 5.0))