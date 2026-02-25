import asyncio
import os

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
#from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from rich import print

import constants

load_dotenv(override=True)
API_HOST=os.getenv("API_HOST", "github")

'''
agent = Agent(
    name="Weather Agent",
    description="Weather Agent",
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
)
'''

if API_HOST == "github":
    client = OpenAIChatClient(
        base_url=constants.GITHUB_AI_URL,
        api_key=os.environ["GITHUB_TOKEN"],
        model_id=os.getenv("GITHUB_MODEL", "openai/gpt-4o-mini")
    )
else:
    print("failed to load the API_HOST")
    exit(1)

agent = Agent(client=client, instructions="You are an information agent. Answer questions cheerfully.")

async def main():
    response = await agent.run("What is the wether in Pesaro?")
    print(response.text)

if __name__ == "__main__":
    print("Start Python Agents")
    asyncio.run(main())