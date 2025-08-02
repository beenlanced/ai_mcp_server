# Creates a simple MCP server to show how to use an MCP server

from pathlib import Path

from fastmcp import FastMCP


# Initialize the MCP server instance with a a descriptive name
mcp = FastMCP("Simple Calculator Server") 


@mcp.tool()
def add(a: int | float, b: int | float) -> int | float:
    """
    Adds two integers together.

    Args:
        a (int | float): first number to add
        b (int | float): second number to add

    Returns:
        int | float: The sum of numbers a and b
    """
    return a + b

@mcp.tool()
def subtract(a: int | float, b: int | float) -> int | float:
    """
    Subtract two numbers. Subtract the second number from the first.

    Args:
        a (int | float): first number to subtract from
        b (int | float): second number to subtract

    Returns:
        int | float: The difference of numbers a and b
    """
    return a - b

@mcp.tool()
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiply two numbers together.

    Args:
        a (int | float): first number to multiply
        b (int | float): second number to multiply

    Returns:
        int | float: The multiplication of numbers a and b
    """
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second. Raises error on division by zero.

    Args:
        a (float): first integer to divide by - the numerator
        b (float): second integer to divide - the denominator

    Returns:
        float: The division of a by b or raises ValueError if b is zero
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

# Add a dynamic greeting resource to the server
# makes greeting://your_name available to the model.
# When the model queries this resource, the function will execute and return the greeting message.
@mcp.resource("calculator://greet/{name}")
def calculator_greeting(name: str) -> str:
    """
    Returns a personalized greeting message for the given name.

    Args:
        name (str): The name to greet

    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to the Simple Calculator Server."


# Adding a static resource to the server
@mcp.resource("usage://guide")
def get_usage_guide() -> str:
    """
    gets the usage guide for the Simple Calculator Server.

    Returns:
        str: A string containing the usage guide for the server.
    """
    # Get the file path of the docs directory
    docs_path = Path(__file__).parent.parent / "docs"
    file_path = (docs_path / "usage.txt").resolve()

    if file_path.is_file():
        with open(file_path, "r") as file:
            return file.read()
    else:
        return "Usage guide not found."

# Creating Prompts   
@mcp.prompt()
def calculator_prompt(a: float, b: float, operation: str) -> str:
    """
    Prompt for a calculation and return the result.

    Args:
        a (float): _description_
        b (float): _description_
        operation (str): _description_

    Returns:
        str: _description_
    """
    if operation == "add":
        return f"The result of adding {a} and {b} is {add(a, b)}"
    elif operation == "subtract":
        return f"The result of subtracting {b} from {a} is {subtract(a, b)}"
    elif operation == "multiply":
        return f"The result of multiplying {a} and {b} is {multiply(a, b)}"
    elif operation == "divide":
        try:
            return f"The result of dividing {a} by {b} is {divide(a, b)}"
        except ValueError as e:
            return str(e)
    else:
        return "Invalid operation. Please choose add, subtract, multiply, or divide."
    


if __name__ == "__main__":
    # Start the MCP server
    #transport = 'stdio' is suitable for local MCP.
    mcp.run()