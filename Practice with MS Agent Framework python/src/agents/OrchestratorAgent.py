from typing import Annotated
from agent_framework import Agent, AgentResponse, tool
from agents import builder
from logging_configuration import log_tool_call


#@dataclass
#class Response:
#    name: Annotated[str, "The city name"]
#    latitude: Annotated[float, "The latitude of the city"]
#    longitude: Annotated[float, "The longitude of the city"]

class OrchestratorAgent:

    def __init__(self, meteo_agent:Agent):
        self.meteo_agent=meteo_agent

        self.name = "Orchestrator"
        self.description = "Agent to manage requests and sub-agents."
        self.instructions = [
            "You are a chereful agent.",
            "You are a supervisor managing specialist agents."
            "Use your tools to answer user questions.",
            "When invoking a tool, provide clear, concise queries.",
            "For questions about the weather use the Meteo tool.",
            "For question about Italian law use the Italia Law tool.",
            "If you think you don't have the right tool for the task, list your tools to the user, format the list in JSON"
        ]

    def get_definition(self): 
         return builder.AgentDefinition(self.name, self.description, self.instructions)    


    @tool(description="Answer messages about the weather.")
    async def ask_Weather(self, question: Annotated[str, "The user message"]): #-> AgentResponse:
        """Returns the agent response about the weather."""
        print("bbbb")
        log_tool_call("ask_Weather", question)
        response = await self.meteo_agent.run(question)
        return response.text

