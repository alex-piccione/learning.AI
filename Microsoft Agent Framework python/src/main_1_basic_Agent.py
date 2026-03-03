import asyncio
import os
import json

#  uv add "agent-framework==1.0.0rc2" --pre
from agent_framework import Agent, exceptions
from agent_framework.openai import OpenAIChatClient
#from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from rich import print

import constants

load_dotenv(override=True)
API_HOST="openai" # github, openai 

if API_HOST == "github":
    client = OpenAIChatClient(
        base_url=constants.GITHUB_AI_URL,
        api_key=os.environ["GITHUB_TOKEN"],
        model_id=os.getenv("GITHUB_MODEL", "openai/gpt-4.1-mini")
    )
elif API_HOST == "openai":
    client = OpenAIChatClient(
        api_key=os.environ["OPENAI_API_KEY"],
        model_id=os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    )
else:
    print("failed to load the API_HOST")
    exit(1)

agent = Agent(client=client, instructions="You are an information agent. Answer questions cheerfully.")


'''
def extract_error(ex):

    #''
    #<class 'agent_framework.openai._chat_client.OpenAIChatClient'> service failed to complete the prompt: Error code: 404 - {
    #'error': {'message': 'The model `gpt-4-mini` does not exist or you do not have access to it.', 
    #'type': 'invalid_request_error', 'param': None, 'code': 'model_not_found'}}
    #''

    error_string = str(ex)
    start = error_string.find("{")
    if start == -1:
        return {"message": error_string, "code": None, "type": None}
    
    json.load(error_string[start...])
'''


async def main():

    try:
        response = await agent.run("What is the weather in Pesaro?")
        print(response.text)
    except exceptions.ChatClientException as ex:
        print(f"ChatClientException. {ex}")
    except Exception as ex:
        print(f"Failed to call Agent. {ex}")

if __name__ == "__main__":
    print("Start Python Agents")
    asyncio.run(main())