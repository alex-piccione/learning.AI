from dataclasses import dataclass
from typing import List


@dataclass
class Result:      
    name: str
    latitude: float
    longitude: float


@dataclass
class SearchResult: 
    results: List[Result]
