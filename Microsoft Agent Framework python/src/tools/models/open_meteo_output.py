from dataclasses import dataclass
from typing import Annotated


@dataclass
class CityGeolocation:
    name: Annotated[str, "The city name"]
    latitude: Annotated[float, "The latitude of the city"]
    longitude: Annotated[float, "The longitude of the city"]



@dataclass
class CurrentWeather:
    temperature: Annotated[float, "Current temperature in °C"]
    wind_speed: Annotated[float, "Current wind speed in km/h"]
    wind_direction: Annotated[str, "Current wind direction"]
    weather_description: Annotated[int, "Weather condition description"]
