from dataclasses import dataclass
from typing import Annotated


@dataclass
class CityGeolocation:
    name: Annotated[str, "The city name"]
    latitude: Annotated[float, "The latitude of the city"]
    longitude: Annotated[float, "The longitude of the city"]