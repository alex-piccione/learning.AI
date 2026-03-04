import asyncio
import os
import agent_builder
from agent_builder import ModelType 
from agent_framework import  exceptions
#from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from rich import print
from normattiva import NormattivaTool

exa_api_key=os.environ["EXA_API_KEY"]
normattiva_tool = NormattivaTool(exa_api_key)

client = agent_builder.get_client(ModelType.REASONING)
agent = client.as_agent(
    name="Italian lawyer",
    instructions = (
        "You are a research assistant. You use Normattiva (www.normattiva.it) to answer questions."
        "You can search laws."
    ),
    tools = normattiva_tool.get_tools()    
)

async def main():    
    print(f"LLM Model: {client.model_id}")  
    try:
        response = await agent.run("What is the law number about the Regime Forfettario? Show me a resume of the law.")
        #response = await agent.run("Give me the first paragraph of the law 100 of December 23, 2014.")
        print(response.text)
    except exceptions.ChatClientException as ex:
        print(f"ChatClientException. {ex}")
    except Exception as ex:
        print(f"Failed to call Agent. {ex}")

if __name__ == "__main__":
    print("Python Agents")
    asyncio.run(main())


    """
    Python Agents
To find the first paragraph of the specific law you're looking for, you should visit the Normattiva website (www.normattiva.it) where you can search for 
Italian laws by their number and date. Simply enter "Legge 23 dicembre 2014, n. 100" into their search function to locate and view the text directly.
 *  Terminal will be reused by tasks, press any key to close it. 
    """