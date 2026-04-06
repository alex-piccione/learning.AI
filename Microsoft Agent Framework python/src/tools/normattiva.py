'''
Normattiva (www.normattiva.it) is teh semi-official website where you can find original and udated italian laws.
Example of URL: "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53").

For search_law it needs an API key for exa.ai.
'''

from agent_framework import tool
from typing import Annotated
from normattiva2md import convert_url, search_law
from ..logging_configuration import log_tool_call

class NormattivaTool:

    def __init__(self, exa_api_key:str):
        self.exa_api_key=exa_api_key

    @tool(description="Fetch and convert the Italian law to Markdown using normattiva.it")
    def get_law_markdown(self, url: Annotated[str, "The URL of normattiva.it"]) -> str:
        """Fetch and convert Italian law to Markdown"""
        log_tool_call("get_law_markdown", f"url={url}")
        result = convert_url(url)
        return result.markdown
    
    @tool(description="Correct the URN:NRI URL because encoded does not work")
    def unencode_urn_nri_url(self, url: Annotated[str, "The URL in URN:NRI format to correct"]) -> str:
        """The returned URL from the serach call is encoded, but the normattiva website accepts only unencode ones."""
        log_tool_call("unencode_urn_nri_url", f"url={url}")
        if ("N2Ls?urn:nir" in url):
            url = url.replace("%3A", ":").replace("%3B", ";").replace("%21", "!")
        return url

    @tool(description="Search a text on normattiva.it")
    #@tool(approval_mode="always_require")
    def search(self, query: Annotated[str, "The text to search"]) -> str:
        """Search laws (needs EXA_API_KEY)"""
        log_tool_call("search", f"query={query}")
        result = search_law(query=query, exa_api_key=self.exa_api_key)
        
        #print("--- start ---")
        print(str(result))
        #print("--- end ---")

        return str(result)  # list of SearchResult objects
    
    def get_tools(self) -> list:
        return [self.get_law_markdown, self.search, self.unencode_urn_nri_url]   #  <-- how to return these tools ?


'''
Result from normattiva.it search contagins 4 links:
 - SearchResult(url='https://www.normattiva.it/eli/stato/LEGGE/2022/12/29/197/CONSOLIDATED', 
             title='LEGGE 29 dicembre 2022, n. 197', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=86&atto.codiceRedazionale=17G00128&atto.dataPubblicazioneGazzetta=2017-08-02&qId=&tabID=0.8298684148665065&title=lbl.dettaglioAtto', 
             title='DECRETO LEGISLATIVO 3 luglio 2017, n. 117', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1%21vig=', 
             title='LEGGE 23 dicembre 2014, n. 190', score=0.0), 
 - SearchResult(url='https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B190%21vig=2023-10-03', 
             title='LEGGE 23 dicembre 2014, n. 190', score=0.0)]

https://www.normattiva.it/eli/stato/LEGGE/2022/12/29/197/CONSOLIDATED:  OK
https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=86&atto.codiceRedazionale=17G00128&atto.dataPubblicazioneGazzetta=2017-08-02&qId=&tabID=0.8298684148665065&title=lbl.dettaglioAtto  OK
https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1%21vig=   ERROR
https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B190%21vig=2023-10-03   ERROR

curl https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014%3B190%7Eart1%21vig=

https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B199%21vig

: -> %3A
; -> %3B
! -> %21

https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190!vig
https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B190%21vig

https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Alegge%3A2014-12-23%3B190
https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190

'''
