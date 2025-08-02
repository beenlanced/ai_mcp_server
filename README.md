### Tools

- `AWS Strands` powerful SDK that takes a model-driven approach to building and running AI agents builds our MCP client
- `FastAPI` wrapped our MCP tools so I can run the app on uvicorn
- `FastMCP`
- `JSON`
- `Node.js` JavaScript runtime environment to help run MCP inspector,
- `NPM` Node Package Manager the default packet manager for Node.js,
- `Gemini AI` - to show Integration with MCP.

## reference

[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file)

[FastMCP](https://gofastmcp.com/getting-started/welcome)

[scrapfly](https://scrapfly.io/blog/posts/how-to-build-an-mcp-server-in-python-a-complete-guide)

[Deploy Remote MCP Servers in Python (Step By Step)](https://www.youtube.com/watch?v=wXAqv8uvY0M#ddg-play)

[Ultimate Guide to Building an MCP Server with FastMCP + Testing with AWS Strands & LangGraph](https://dragonforest.in/mcp-server-with-fastmcp/)

[Learn MCP Servers with Python (EASY)](https://www.youtube.com/watch?v=Ek8JHgZtmcI)

[Understanding MCP Basics](https://www.youtube.com/watch?v=5xqFjh56AwM)
using remote server

[MCP Crash Course for Python Developers](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course) ----this one

[Model Context Protocol(MCP) with Google Gemini 2.5 Pro — A Deep Dive (Full Code)](https://medium.com/google-cloud/model-context-protocol-mcp-with-google-gemini-llm-a-deep-dive-full-code-ea16e3fac9a3)

[LangChain MCP Adapters](https://timtech4u.medium.com/zero-to-mcp-hero-building-multi-tool-ai-agents-in-python-gemini-c181fbb047b7)

### Github

https://github.com/beenlanced/ai_mcp_server.git

### Prerequistes

- To run MCP inspector you will need to make sure you have [Node.js](https://nodejs.org/en/download) and [NPM](https://nodejs.org/en/download) installed on your machine.

- Set up your Gemini AI API key in a `.env` file. See `.env.example` as an example

- install google-genai

### Running the MCP server

I have wrapped our MCP tools in FastAPI, so we can run the app on uvicorn and can do a health check of our MCP server when we deploy it on the server.

- To test the MCP server using MCP inspector. Open up a command terminal. Navigate to the directory containing a the server file. At the command line enter

```bash
mcp dev demo_server.py
```

Or alternatively

```bash
fastmcp dev demo_server.py
```

Once you close out of MCP inspector to fully kill the process use the following steps (here shown for Linux/MacOS)

    - get the process id of the process using the MCP inspector and occupying the port

    ```bash
    lsof -i:6277
    ```

    Resulting in

    ```
    COMMAND   PID        USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    node    15914 username   13u  IPv6 0x1f996f3347e2cb0c      0t0  TCP localhost:6277 (LISTEN)
    ```

    - terminate the proecess id (PID)

    ```bash
    kill -9 15914
    ```

    This should free up the port for future new executions of the MCP inspector. In the case, that the port is still that you still receive `Proxy Server PORT IS IN USE at port 6277` try the above steps and additionally close out of the IDE you are using. Reopen the IDE and try launching MCP inspector.

first start it by running the following command after navigating to the `src/` folder first

```bash
    uv run uvicorn simple_calc_server:app
```

This will start our app at _http://127.0.0.1:8000_ (this host URL will be used for establishing a connection).
In a browser, confirm the health of the server using

```
http://127.0.0.1:8000/health
```

should see

```
{"status":"healthy"}
```

- Use `AWS Strands`
