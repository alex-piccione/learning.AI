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
        print("******** tool:  get_law_markdown ********")
        print(f"URL: {url}")
        result = convert_url(url)
        return result.markdown

    @tool(description="Search a text on normattiva.it")
    #@tool(approval_mode="always_require")
    def search(self, query: Annotated[str, "The text to search"]) -> str:
        """Search laws (needs EXA_API_KEY)"""
        print("******** tool: search ********")
        result = search_law(query=query, exa_api_key=self.exa_api_key)

        #print("--- start ---")
        print(str(result))
        #print("--- end ---")

        return str(result)  # list of SearchResult objects
    
    def get_tools(self) -> list:
        return [self.get_law_markdown, self.search]   #  <-- how to return these tools ?


'''
Result from normayyiva.it search contagins 4 links:
 - SearchResult(url='https://www.normattiva.it/eli/stato/LEGGE/2022/12/29/197/CONSOLIDATED', 
             title='LEGGE 29 dicembre 2022, n. 197', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=86&atto.codiceRedazionale=17G00128&atto.dataPubblicazioneGazzetta=2017-08-02&qId=&tabID=0.8298684148665065&title=lbl.dettaglioAtto', 
             title='DECRETO LEGISLATIVO 3 luglio 2017, n. 117', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1%21vig=', 
             title='LEGGE 23 dicembre 2014, n. 190', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B190%21vig=2023-10-03', 
             
This one seems wrong to me:
https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1%21vig=

https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1&vig=

'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             title='LEGGE 23 dicembre 2014, n. 190', score=0.0)]