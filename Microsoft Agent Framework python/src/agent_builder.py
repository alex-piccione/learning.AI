from dotenv import load_dotenv
from agent_framework.openai import OpenAIChatClient
import constants
import os

load_dotenv(override=True)
API_HOST="openai" # github, openai 

def get_client():

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
        #raise("failed to load the API_HOST")
        exit(1)

    return client