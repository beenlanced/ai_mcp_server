# demo_server.py
from mcp.server.fastmcp import FastMCP # using mcp first 


# Create an MCP server
mcp = FastMCP(
    name="DemoServer",
    host="127.0.0.1", # For Streamable-http and 0.0.0.0 for SSE transport (localhost)
    port=8050, # Only used for Streamable-http and SSE transport (set this to any port)
    stateless_http=True
    )

# Simple tool
@mcp.tool()
def say_hello(name: str) -> str:
    """
    Say hello to someone

    Args:
        name(str): The person's name to greet

    Returns:
        str: Returns a string saying hello
    """
    return f"Hello, {name}! Nice to meet you."

# Run the server
if __name__ == "__main__":
    # Using the STDIO method which is default in mcp.run()
    transport = "streamable-http"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse": #Server Sent Events (SSE)
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")