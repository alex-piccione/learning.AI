# Python Agents



https://github.com/Azure-Samples/python-agentframework-demos




## Python AI frameworks

- agent_framework  is a framework from Microsoft (successor of semantic-kernel) well integratd with Azure
- langchain v1   (similar to agent_framework)
- pydantic-ai
- openai-agent

uv run   and uv sync ???


install agen _-core and  _-ui




## venv

`python -m venv agents` creates a virtialenv named "agents"  
It created a folder named "agents". I renamed that folder "venv_agents" for clarity.  

`./venv_agents/Scripts/activate` will activate it  


## 

import asyncio
import os

from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from rich import print