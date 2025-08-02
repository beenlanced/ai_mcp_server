from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # For Streamable-http and 0.0.0.0 for SSE transport (localhost)
    port=8050,  # Only used for Streamable-http and SSE transport (set this to any port)
    stateless_http= True
)

# Add a simple calculator tool
@mcp.tool()
def add(a: int| float, b: int | float) -> int | float:
    """Add two numbers together

    Args:
        a (int | float): first number
        b (int | float): second number

    Returns:
        int | float: sum of the first and second number
    """
    return a + b


# Run the server
if __name__ == "__main__":
    print("Running server with Streamable HTTP transport")
    mcp.run(transport="streamable-http")