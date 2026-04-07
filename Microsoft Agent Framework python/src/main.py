import asyncio
import os
import logging
from client_wrapper import ApiHost, ModelType, create_client
from agent_framework import  exceptions
# from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from rich import print
from logging_configuration import setup_logging
from tools import tools_builder
from tools.normattiva import NormattivaTools
from tools.open_meteo import OpenMeteoTools

setup_logging()

exa_api_key=os.environ["EXA_API_KEY"]
normattiva_tools = NormattivaTools(exa_api_key)
open_meteo_tools = OpenMeteoTools()

tools = tools_builder.discover_tools(normattiva_tools, open_meteo_tools)

client_reasoning = create_client(ApiHost.AliBaba, ModelType.REASONING)
client_cheap = create_client(ApiHost.AliBaba, ModelType.CHEAP)
client_fast = create_client(ApiHost.AliBaba, ModelType.FAST)

logging.info(f"LLM Model for client_reasoning: {client_reasoning.model} from {client_reasoning.api_host}")  
logging.info(f"LLM Model for client_cheap: {client_cheap.model} from {client_cheap.api_host}")  
logging.info(f"LLM Model for client_fast: {client_fast.model} from {client_fast.api_host}")  

lawyer_agent = client_reasoning.as_agent(
    name="Italian lawyer",
    instructions = (
        "You are a research assistant. You use Normattiva (www.normattiva.it) to answer questions."
        "You can search laws."
    ),
    tools = tools      
)

meteo_agent = client_cheap.as_agent(
    name="Colonnello Bernacca",
    instructions=(
        "You are an expert metereologyst.",
        "You use your tools to answer user questions,"
    ),
    tools = tools
)


async def main():    

    try :
        response = await meteo_agent.run("Che tempo fa a Pesaro, in Italia?")
        #response = await meteo_agent.run("Dove si trova Pesaro, in Italia?")
        print(response.text)
    except exceptions.ChatClientException as ex:
        logging.error(f"ChatClientException. {ex}")
    except Exception as ex:
        logging.error(f"Failed to call Agent. {ex}")
    
    return 0

    try:
        response = await lawyer_agent.run("What is the law number about the Regime Forfettario? Show me a resume of the law.")
        #response = await agent.run("Give me the first paragraph of the law 100 of December 23, 2014.")
        print(response.text)
    except exceptions.ChatClientException as ex:
        logging.error(f"ChatClientException. {ex}")
    except Exception as ex:
        logging.error(f"Failed to call Agent. {ex}")

if __name__ == "__main__":
    print("Python Agents")
    asyncio.run(main())
    
