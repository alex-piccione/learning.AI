# Python Agents

Microsoft course:  
Python + Agents: Building AI agents and workflows with Agent Framework  

https://developer.microsoft.com/en-us/reactor/series/S-1631  

- 1. Python + Agents: Building your first agent in Python
  https://www.youtube.com/live/I4vCp9cpsiI
- 2. Python + Agents: Adding context and memory to agents
  https://www.youtube.com/live/BMzI9cEaGBM
- 3. Python + Agents: Monitoring and evaluating agents
  https://developer.microsoft.com/en-us/reactor/events/26690?event_check_in=PSvVYum%206SMLKSjWTqjsJHN8OYg4wZDOGYByqWx76o5/u2hNfRANxd3ofO5CgrkPTxN3QnFA86STI91b%206hnAg==
  https://www.youtube.com/live/3yS-G-NEBu8

- 4. Python + Agents: Building your first AI-driven workflows
  https://www.youtube.com/live/FQtZCKWjARI
- 5. 
- 6.

  
Repository:  
https://github.com/Azure-Samples/python-agentframework-demos
  
Recording  & Resources:  
https://github.com/orgs/microsoft-foundry/discussions/280


Boot.dev: Build an AI Agent: https://www.boot.dev/lessons/44e182d7-c2c6-4c7e-9313-1b078e301344




## Run the examples

Code is in _src_ folder.  
The _examples_ flder contain examples from Google demo repo: https://github.com/Azure-Samples/python-agentframework-demos

Vis ed to run the Pyton app. 
I'll try to put the new improved code in main.py, to run it: ``uv run src/main.py``.  



## Python AI frameworks

- agent_framework is a framework from Microsoft (successor of semantic-kernel) well integratd with Azure
- langchain v1  (similar to agent_framework)
- pydantic-ai   
- openai-agent  (more limited)


## venv

`python -m venv .venv` creates a virtualenv named ".venv"  and the folder _.venv_.  
`source ./.venv/Scripts/activate` will activate it in current shell

Don't try to use a different name!  
You need to update some files manually and add instruction to avery command (also to UV) and it does nto work or will not work in the future, a nightmare!

## UV

``uv buid`` to build the project.  
``uv add <library>`` to adda library  


## Issues

### Getting AttributeError: type object 'SpanAttributes' has no attribute 'LLM_SYSTEM'

agent-framework version 1.0.0-rc1  raises an error for missing LLM_ attribute or something like that.  
The solution was to downgrade "opentelemetry-semantic-conventions-ai":  
`uv add opentelemetry-semantic-conventions-ai==0.4.13`  


## Open AI models

gpt-5.1
gpt-5-mini
gpt-5-nano
gpt-4.1
gpt-4.1-mini
o4-mini


## DEV UI

``uv run <fiel> --devui``


## Session 1

What is an Agent?  
**An Agent is an LLm thta runs tools ina loop to achieve a goal.**  

agent_basic.py


## Context

### Memory

Session (LLM memory)
- truncation and summarization
- can be stored in memory or on the database

- Chat history
  Stored in database the user previous chat(s)

agent_session.py
   session can be sgared by agents 

- Dynamic memory
  Stored in database
  Searched and Retrieved when specifically asked


Mem0 us a "provier" that manage also response to add/delete/upate the memory



- Knowledge provider
  it executes ALAYs, and before the tools. 
  It retrieve information, always, that are added to the context




# 3



# 4 Worflows


workflow_aggregator_structured.py  : workflow without an LLm  at all

```python
from agent_framework.devui import serve
serve
```

workflow_agents.py  : workflow with agents


Branching. workflow_conditional_.p


Structured Output.  workflow_conditional_structured.py


Swith-case conditions.

State management. workflow_conditional_state.py  ctx.set_state/get_state

