# Alternate Simple Server Project

This project demonstrates how you could create a file to test that an MCP server is working. It is mostly to help out during development. It is a simple example of how to build an easy Python coded client to access tools from the MCP server using the STDIO transport. Notice, no Large Language Models (LLMs) were involved.

## Project Structure

- `simple_calc_server.py`: The MCP server implementation with a simple calculator tools (add, subtract, multiply, etc.)
- `test_mcp_server.py`: A client that connects to the server and calls the calculator tool

## Running with test_mcp_server.py

To run

- Navigate to the directory where `test_mcp_server.py` exists
- In a NEW terminal, at the command line, execute `uv run test_mcp_server.py`

Make sure:

1. The server is running before running this `test_mcp_server.py` script.
2. The server is configured to use STDIO transport in `simple_calc_server.py`.
3. Navigate to the directory where `simple_calc_server.py` exists.

   To run the server:

   ```bash
   uv run simple_calc_server.py
   ```

The test client will connect to the server and use the calculator's divide tool to divide 10.0 by 5.0.
