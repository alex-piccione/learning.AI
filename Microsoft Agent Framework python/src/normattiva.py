'''
Normattiva (www.normattiva.it) is teh semi-official website where you can find original and udated italian laws.
Example of URL: "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53").

For search_law it needs an API key for exa.ai.
'''

from agent_framework import tool
from typing import Annotated
from normattiva2md import convert_url, search_law

class NormattivaTool:

    def __init__(self, exa_api_key:str):
        self.exa_api_key=exa_api_key

    @tool(description="Fetch and convert the Italian law to Markdown using normattiva.it")
    def get_law_markdown(self, url: Annotated[str, "The URL of normattiva.it"]) -> str:
        """Fetch and convert Italian law to Markdown"""
        result = convert_url(url)
        return result.markdown

    @tool(description="Search a text on normattiva.it")
    #@tool(approval_mode="always_require")
    def search(self, query: Annotated[str, "The text to search"]) -> str:
        """Search laws (needs EXA_API_KEY)"""
        result = search_law(query=query, exa_api_key=self.exa_api_key)
        return str(result)  # list of SearchResult objects
    
    def get_tools(self) -> list:
        [self.get_law_markdown, self.search]   #  <-- how to return these tools ?
