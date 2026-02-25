# Python Agents

Microsoft course:  
Python + Agents: Building AI agents and workflows with Agent Framework  

https://developer.microsoft.com/en-us/reactor/series/S-1631  

Repository:  
https://github.com/Azure-Samples/python-agentframework-demos



## Python AI frameworks

- agent_framework  is a framework from Microsoft (successor of semantic-kernel) well integratd with Azure
- langchain v1   (similar to agent_framework)
- pydantic-ai
- openai-agent

uv run   and uv sync ???


install agen _-core and  _-ui




## venv

`python -m venv .venv_agents` creates a virtualenv named ".venv_agents"  and the folder _.venv_agents_.  

`source ./.venv_agents/Scripts/activate` will activate it in current shell



UV_PROJECT_ENVIRONMENT=".venv_agents" uv add rich python-dotenv


## UV

To make UV able to use the existing .venv_agents folder instead of the expected .venv:  
`UV_PROJECT_ENVIRONMENT=".venv_agents" uv add rich python-dotenv`  
or  
`export UV_PROJECT_ENVIRONMENT=".venv_agents"`  


## Issues

### Getting AttributeError: type object 'SpanAttributes' has no attribute 'LLM_SYSTEM'

agent-framework version 1.0.0-rc1  raises an error for missing LLM_ attribute or something like that.  
The solution was to downgrade "opentelemetry-semantic-conventions-ai":  
`UV_PROJECT_ENVIRONMENT=".venv_agents" uv add opentelemetry-semantic-conventions-ai==0.4.13`  
