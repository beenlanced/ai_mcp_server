import json
import os

from openai import OpenAI
from dotenv import load_dotenv
from tools import add


load_dotenv("../.env")

"""
This example demonstrate how MCP enables a new way to call functions.
"""

# Define tools for the model
tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "First number"},
                    "b": {"type": "integer", "description": "Second number"},
                },
                "required": ["a", "b"],
            },
        },
    }
]

# Authenticate abd configure the API Client
# https://ai.google.dev/gemini-api/docs/openai
gemini_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Initialize the Model
model = "gemini-2.5-flash"

# Create a prompt/message
content = "Calculate 25 + 17"

# Call LLM

response = gemini_client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Calculate 25 + 17"}],
    tools=tools,
)

if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    tool_name = tool_call.function.name
    tool_args = json.loads(tool_call.function.arguments)

    # Execute directly
    result = add(**tool_args)

    # Send result back to model
    final_response = gemini_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": "Calculate 25 + 17"},
            response.choices[0].message,
            {"role": "tool", "tool_call_id": tool_call.id, "content": str(result)},
        ],
    )
    print(final_response.choices[0].message.content)