from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient
import constants
import os
import logging
from enum import Enum

# helper for create AI Client that can be used to creatre Agents

load_dotenv(override=True)

class ApiHost(Enum):
    AliBaba = 1
    AliBaba_Plan = 2
    GitHub = 3
    OpenAI = 4

class ModelType(Enum):
    REASONING = 1
    FAST = 2
    CHEAP = 3

def create_client(api_host: ApiHost, model_type: ModelType) -> OpenAIChatClient:
    """
    Creates and returns an OpenAIChatClient instance based on the specified model type and API host.
    
    This function initializes a client for interacting with different AI service providers 
    (GitHub, OpenAI, or Alibaba) depending on the configured API_HOST environment setting.
    The client returned will be configured with the appropriate API key, base URL, and model ID
    based on the requested model type.
    
    Args:
        api_host (ApiHost): ...

        model_type (ModelType): The type of model to use. Can be one of:
            - ModelType.REASONING: For reasoning-intensive tasks
            - ModelType.FAST: For faster processing
            - ModelType.CHEAP: For cost-effective processing
    
    Returns:
        OpenAIChatClient: An initialized client object configured according to the 
        specified model type and the current API_HOST setting.
        
    Raises:
        SystemExit: If an unsupported API_HOST is configured, the function will 
        print an error message and exit the program.
    """

    if api_host == ApiHost.GitHub:
        model_key = "GITHUB_MODEL"
        client = OpenAIChatClient(
            base_url=constants.GITHUB_AI_URL,
            api_key=os.environ["GITHUB_TOKEN"],
            model=os.getenv(model_key)
        )
    elif api_host == ApiHost.OpenAI:
        model_key = {
            ModelType.REASONING: "OPENAI_MODEL",
            ModelType.FAST: "OPENAI_MODEL_FAST",
            ModelType.CHEAP: "OPENAI_MODEL_CHEAP"
        }.get(model_type, "OPENAI_MODEL")

        client = OpenAIChatClient(
            api_key=os.environ["OPENAI_API_KEY"],
            model=os.getenv(model_key)
        )
    elif api_host == ApiHost.AliBaba:
        model_key = {
            ModelType.REASONING: "ALIBABA_MODEL",
            ModelType.FAST: "ALIBABA_MODEL_FAST",
            ModelType.CHEAP: "ALIBABA_MODEL_CHEAP"
        }.get(model_type, "ALIBABA_MODEL")

        client = OpenAIChatClient(
            base_url=constants.ALIBABA_AI_URL,
            api_key=os.environ["ALIBABA_API_KEY"],
            model=os.getenv(model_key)
        )
    elif api_host == ApiHost.AliBaba_Plan:
        model_key = {
            ModelType.REASONING: "ALIBABA_PLAN_MODEL",
            ModelType.FAST: "ALIBABA_PLAN_MODEL_FAST",
            ModelType.CHEAP: "ALIBABA_PLAN_MODEL_CHEAP"
        }.get(model_type, "ALIBABA_PLAN_MODEL")

        client = OpenAIChatClient(
            base_url=constants.ALIBABA_PLAN_AI_URL,
            api_key=os.environ["ALIBABA_PLAN_API_KEY"],
            model=os.getenv(model_key)
        )
    else:        
        logging.error("failed to load the API_HOST")
        #raise("failed to load the API_HOST")
        exit(1)

    return client
