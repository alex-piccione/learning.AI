import os

from agent_framework import Agent

from agents.OrchestratorAgent import OrchestratorAgent
from client_builder import ApiHost, ModelType, create_client
from tools import tools_builder
from tools.open_meteo import OpenMeteoTools


from dataclasses import dataclass

## TODO: create a base class for Agent
@dataclass(frozen=True)
class AgentDefinition:
    name: str
    description: str
    instructions: str | list[str]

class AgentBuilder():

    client_reasoning = create_client(ApiHost.AliBaba, ModelType.REASONING)
    client_cheap = create_client(ApiHost.AliBaba, ModelType.CHEAP)
    client_fast = create_client(ApiHost.AliBaba, ModelType.FAST)

    #tools = tools_builder.discover_tools(normattiva_tools, open_meteo_tools)

    exa_api_key=os.environ["EXA_API_KEY"]
    #normattiva_tools = NormattivaTools(exa_api_key)
    open_meteo_tools = OpenMeteoTools().get_tools()

    def build_cheap(self, definition:AgentDefinition, tools) -> Agent:

        return self.client_cheap.as_agent(
            name=definition.name,
            description=definition.description,
            instructions=definition.instructions,
            tools = tools
        )
    
    def build_smart(self, definition:AgentDefinition, tools) -> Agent:

        return self.client_reasoning.as_agent(
            name=definition.name,
            description=definition.description,
            instructions=definition.instructions,
            tools = tools
        )


    def buildOrchestrator(self) -> Agent:

        agent = OrchestratorAgent(
            meteo_agent=self.buildMeteoAgent()
            )

        tools = tools_builder.discover_tools(agent)

        return self.build_cheap(agent.get_definition(), tools)


    def buildMeteoAgent(self) -> Agent:        
            
        meteo_agent = self.client_cheap.as_agent(
            name="Colonnello Bernacca",
            instructions=(
                "You are an expert metereologyst.",
                "You use right tools to answer the user questions, and if you haven't a proper tool inform the user"
            ),
            tools = self.open_meteo_tools
        )

        return meteo_agent