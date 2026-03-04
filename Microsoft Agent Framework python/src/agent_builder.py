from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient
import constants
import os
from enum import Enum

load_dotenv(override=True)
API_HOST="alibaba" # github, openai, alibaba

class ModelType(Enum):
    REASONING = 1
    FAST = 2
    CHEAP = 3

def get_client(model_type: ModelType) -> OpenAIChatClient:

    if API_HOST == "github":
        model_key = "GITHUB_MODEL"
        client = OpenAIChatClient(
            base_url=constants.GITHUB_AI_URL,
            api_key=os.environ["GITHUB_TOKEN"],
            model_id=os.getenv(model_key)
        )
    elif API_HOST == "openai":
        model_key = {
            ModelType.REASONING: "OPENAI_MODEL",
            ModelType.FAST: "OPENAI_MODEL_FAST",
            ModelType.CHEAP: "OPENAI_MODEL_CHEAP"
        }.get(model_type, "OPENAI_MODEL")

        client = OpenAIChatClient(
            api_key=os.environ["OPENAI_API_KEY"],
            model_id=os.getenv(model_key)
        )
    elif API_HOST == "alibaba":
        model_key = {
            ModelType.REASONING: "ALIBABA_MODEL",
            ModelType.FAST: "ALIBABA_MODEL_FAST",
            ModelType.CHEAP: "ALIBABA_MODEL_CHEAP"
        }.get(model_type, "ALIBABA_MODEL")

        client = OpenAIChatClient(
            base_url=constants.ALIBABA_AI_URL,
            api_key=os.environ["ALIBABA_API_KEY"],
            model_id=os.getenv(model_key)
        )
    else:        
        print("failed to load the API_HOST")
        #raise("failed to load the API_HOST")
        exit(1)

    return client