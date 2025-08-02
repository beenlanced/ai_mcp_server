import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP


#Create the MCP server
mcp = FastMCP(
    name = "Knowlege Base",
    host = "0.0.0.0", # used for streamable-http and SSE transports
    port = 8050, # only used for streamable-http and SSE transports (set to any port desired)
)


@mcp.tool()
def get_knowledge_base() -> str:
    """
    Retrieve the entire knowledge base as a formatted string.

    Returns:
        str: A formatted string containing all Q&A pairs from the knowledge base
    """

    try:
        data_path = Path(__file__).parent / "data"
        file_path = (data_path / "kb.json").resolve()
        with open(file_path, "r") as f:
            kb_data = json.load(f)
        
        # Format the knowledge base a string
        kb_text = "Here is the retrieved knowledge base:\n\n"

        if isinstance(kb_data, list):
            for i, item in enumerate(kb_data, 1):
                if isinstance(item, dict):
                    question = item.get("question", "Unknown question")
                    answer = item.get("answer", "Unkown answer")
                else:
                    question = f"Item {i}"
                    answer = str(item)
                
                kb_text += f"Q{i}: {question}\n"
                kb_text += f"A{i}: {answer}\n\n"
        else:
            kb_text += f" Knowledge base content: {json.dumps(kb_data, indent=2)}\n\n"

        return kb_text
    
    except FileNotFoundError:
        return "Error: Knowledge base file not found"
    except json.JSONDecodeError:
        return "Error: Invlalid JSON in knowledge base file"
    except Exception as e:
        return f"Error: {str(e)}"


#Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio") 