from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient
import constants
import os
import logging
from enum import Enum
from typing import Optional

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

class OpenAIChatClientWrapper:
    """
    A wrapper class for OpenAIChatClient that exposes the API host and model type.
    """
    
    def __init__(self, api_host: ApiHost, model_type: ModelType):
        """
        Initialize the wrapper with the specified API host and model type.
        
        Args:
            api_host (ApiHost): The API host to use
            model_type (ModelType): The type of model to use
        """
        self.api_host = api_host
        self.model_type = model_type
        self._client = self._create_client()
    
    def _create_client(self) -> OpenAIChatClient:
        """
        Creates and returns an OpenAIChatClient instance based on the specified model type and API host.
        
        This function initializes a client for interacting with different AI service providers 
        (GitHub, OpenAI, or Alibaba) depending on the configured API_HOST environment setting.
        The client returned will be configured with the appropriate API key, base URL, and model ID
        based on the requested model type.
        
        Returns:
            OpenAIChatClient: An initialized client object configured according to the 
            specified model type and the current API_HOST setting.
            
        Raises:
            SystemExit: If an unsupported API_HOST is configured, the function will 
            print an error message and exit the program.
        """

        if self.api_host == ApiHost.GitHub:
            model_key = "GITHUB_MODEL"
            client = OpenAIChatClient(
                base_url=constants.GITHUB_AI_URL,
                api_key=os.environ["GITHUB_TOKEN"],
                model=os.getenv(model_key)
            )
        elif self.api_host == ApiHost.OpenAI:
            model_key = {
                ModelType.REASONING: "OPENAI_MODEL",
                ModelType.FAST: "OPENAI_MODEL_FAST",
                ModelType.CHEAP: "OPENAI_MODEL_CHEAP"
            }.get(self.model_type, "OPENAI_MODEL")

            client = OpenAIChatClient(
                api_key=os.environ["OPENAI_API_KEY"],
                model=os.getenv(model_key)
            )
        elif self.api_host == ApiHost.AliBaba:
            model_key = {
                ModelType.REASONING: "ALIBABA_MODEL",
                ModelType.FAST: "ALIBABA_MODEL_FAST",
                ModelType.CHEAP: "ALIBABA_MODEL_CHEAP"
            }.get(self.model_type, "ALIBABA_MODEL")

            client = OpenAIChatClient(
                base_url=constants.ALIBABA_AI_URL,
                api_key=os.environ["ALIBABA_API_KEY"],
                model=os.getenv(model_key)
            )
        elif self.api_host == ApiHost.AliBaba_Plan:
            model_key = {
                ModelType.REASONING: "ALIBABA_PLAN_MODEL",
                ModelType.FAST: "ALIBABA_PLAN_MODEL_FAST",
                ModelType.CHEAP: "ALIBABA_PLAN_MODEL_CHEAP"
            }.get(self.model_type, "ALIBABA_PLAN_MODEL")

            client = OpenAIChatClient(
                base_url=constants.ALIBABA_PLAN_AI_URL,
                api_key=os.environ["ALIBABA_PLAN_API_KEY"],
                model=os.getenv(model_key)
            )
        else:        
            logging.error(f"Unmanaged Api Host: {self.api_host}.")
            raise ValueError(f"Unmanaged Api Host: {self.api_host}")

        return client
    
    @property
    def model(self) -> str:
        """Get the model name from the underlying client."""
        return self._client.model
    
    @property
    def base_url(self) -> Optional[str]:
        """Get the base URL from the underlying client."""
        return getattr(self._client, 'base_url', None)
    
    def as_agent(self, *args, **kwargs):
        """Delegate the as_agent method to the underlying client."""
        return self._client.as_agent(*args, **kwargs)
    
    def __getattr__(self, name):
        """
        Delegate all other attribute access to the underlying client.
        This allows the wrapper to behave like the original OpenAIChatClient.
        """
        return getattr(self._client, name)
    
    def __repr__(self):
        return f"OpenAIChatClientWrapper(api_host={self.api_host}, model_type={self.model_type}, model='{self.model}')"


def create_client(api_host: ApiHost, model_type: ModelType) -> OpenAIChatClientWrapper:
    """
    Creates and returns an OpenAIChatClientWrapper instance based on the specified model type and API host.
    
    Args:
        api_host (ApiHost): The API host to use
        model_type (ModelType): The type of model to use
        
    Returns:
        OpenAIChatClientWrapper: A wrapper around OpenAIChatClient with exposed API host and model type
    """
    return OpenAIChatClientWrapper(api_host, model_type)