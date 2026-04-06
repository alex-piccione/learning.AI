import asyncio
import os
import logging
import agent_builder
from agent_builder import ModelType 
from agent_framework import  exceptions
#from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
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

client = agent_builder.get_client(ModelType.REASONING)
lawyer_agent = client.as_agent(
    name="Italian lawyer",
    instructions = (
        "You are a research assistant. You use Normattiva (www.normattiva.it) to answer questions."
        "You can search laws."
    ),
    tools = tools   
)

async def main():    
    logging.info(f"LLM Model: {client.model_id}")  
    try:
        response = await lawyer_agent.run("What is the law number about the Regime Forfettario? Show me a resume of the law.")
        #response = await agent.run("Give me the first paragraph of the law 100 of December 23, 2014.")
        print(response.text)
    except exceptions.ChatClientException as ex:
        logging.error(f"ChatClientException. {ex}")
    except Exception as ex:
        logging.error(f"Failed to call Agent. {ex}")

if __name__ == "__main__":
    asyncio.run(main())
    print("Python Agents")

    """
    Python Agents
To find the first paragraph of the specific law you're looking for, you should visit the Normattiva website (www.normattiva.it) where you can search for 
Italian laws by their number and date. Simply enter "Legge 23 dicembre 2014, n. 100" into their search function to locate and view the text directly.
 *  Terminal will be reused by tasks, press any key to close it. 
    """