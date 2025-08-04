# Google Gemini AI Integration with MCP

This directory contains folders that demonstrate how to integrate the Model Context Protocol (MCP) with Gemini AI to create a system where the Gemini AI can access and use tools provided by my MCP server.

## Overivew

The following files will show how to:

1. Create an MCP server that exposes a knowledge base tool.

2. Connect Gemini AI to this MCP server

3. Allow Gemini AI to dynamically use the tools when responding to user queries

## Connection Methods

I use the `STDIO` transport for communication between the client and server, which basically means:

- The client and server will run in the same process

- The client launches the server as a subprocess

- No separate server process is needed.

Alternatively, I could split the client and server into separate applications (e.g., running the server on a different machine) by using `streamable-http transport` (Server-Sent Events (SSE) has been deprecated).

## Description of the Data Flow

1.**UserQuery**: The user sends a query to the system like "How to turn on a IPOD shuffle" 2.**Gemini AI API**: The Gemini AI API receives the query and available tools from the MCP server 3.**Tool Selection**: Gemini AI, acting as the reasoning component, decides which tools to use based on the query 4.**MCP Client**: The client receives Gemini AI's tool call request and forwards it to the MCP server (i.e., the appropriate tool) 5.**MCP Server**: The server executes the request tool (e.g., retrieving info from a database) 6.**Response Flow**: The tool result flows back through the MCP client to the Gemini AI model 7.**Final Response**: Gemini AI generates a final response incorporating the tool data.

## How Gemini AI Executes the Tools

Gemini AI function calling mechanism works with MCP tools through these steps:

1. **Tool Registration**: The MCP client converts MCP tools to Gemini AI's function format
2. **Tool Choice**: Gemini AI decides which tools to use based on the user query
3. **Tool Execution**: The MCP client executes the selected tools and returns results
4. **Context Integration**: Gemini AI incorporates the tool results into its response

## The Role of MCP

MCP serves as a standardized bridge between AI models and your backend systems:

- **Standardization**: MCP provides a consistent interface for AI models to interact with tools
- **Abstraction**: MCP abstracts away the complexity of your backend systems
- **Security**: MCP allows you to control exactly what tools and data are exposed to AI models
- **Flexibility**: You can change your backend implementation without changing the AI integration

## Implementation Details

### Server (`server.py`)

The MCP server exposes a `get_knowledge_base` tool that retrieves Q&A pairs from a JSON file.

### Client (`client.py`)

The client:

1. Connects to the MCP server
2. Converts MCP tools to Gemini AI's function format
3. Handles the communication between Gemini AI and the MCP server
4. Processes tool results and generates final responses

### Knowledge Base (`data/kb.json`)

Contains Q&A pairs about company policies that can be queried through the MCP server.

## Running the Example

1. Ensure you have the required dependencies installed
2. Set up your Gemini AI API key in an `.env` file
3. Run the client: `python client.py` from a terminal window
   - alternately, `uv run client.py` also should work.

Note: With the `STDIO` transport used in this example, you don't need to run the server separately as the client will automatically start it.
