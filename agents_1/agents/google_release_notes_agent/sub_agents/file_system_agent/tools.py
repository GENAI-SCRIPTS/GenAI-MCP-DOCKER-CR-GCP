from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset,StdioServerParameters
import asyncio

async def setup_mcp_for_file_system():
    tools,exit_stack = MCPToolset(
        connection_params = StdioServerParameters(
            command = 'npx',
            args = ['-y','@modelcontextprotocol/server-filesystem']
        )
    )
    return tools,exit_stack