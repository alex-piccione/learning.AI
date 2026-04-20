# Examples

Examples from https://github.com/Azure-Samples/python-agentframework-demos.

## Session 1
- agent_basic.py: Basic example of Agent without any Tool
- openai_tool_calling.py: define the tool and call it manually
- agent_tool.py: Agent is capable to have defined tools in a very easy way
- agent_tools.py: give multiple tools to the agent
- agent_mcp_local.py + mcp_server.py: Call a local MCP server
  ``uv run mcp_server.py`` will launch a MCP server locally
  agent_mcp_local.py will use it
  To have this working with .Net MCP client it has to use SSE instead of Streamable-http
- agent_mcp_remote.py: call a MCP remote server
- agent_middleware.py: examples of middlewares
- agent_supervisor.py: supervisor agent that, based on tool call use an agent ot another agent.


## Session 2
- 