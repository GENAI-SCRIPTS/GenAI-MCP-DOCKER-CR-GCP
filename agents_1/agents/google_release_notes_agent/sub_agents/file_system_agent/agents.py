from google.adk.agents import Agent
#from tools import setup_mcp_for_file_system
import asyncio
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset,StdioServerParameters,StdioConnectionParams




def filesystem_root_agent():
     #file_mcp_tools,exit_stack =  setup_mcp_for_file_system()

     root_agent = Agent(
              name = "Filesystem_agent",
              tools =[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command = 'npx',
                    args = ['-y','@modelcontextprotocol/server-filesystem','C:\Source_code\Google_release_notes_github\GenAI-MCP-DOCKER-CR-GCP'],
                ),
            ),
            # You can filter for specific Maps tools if needed:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
    ],
              description="An agent that can interact with filesystem",
              instruction="You are a system admin having access to all directories.You are required to perform actions in filesystem as per user input. Please take confirmation from user before making any changes ",
              model='gemini-2.5-flash',
       )
     
     return root_agent

if __name__ == "__main__":
     root_agent = filesystem_root_agent()
     print("Agent Created:",root_agent.name)