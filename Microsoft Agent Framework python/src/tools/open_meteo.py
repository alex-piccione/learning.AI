from agent_framework import tool
from typing import Annotated
import requests
import logging
from ..logging_configuration import log_tool_call

from .models.open_meteo_api import SearchResult, Result
from .models.open_meteo_output import CityGeolocation


class OpenMeteoTool:

    apiUrlBase = "https://api.open-meteo.com/v1"
    geolocationApiBaseUrl = "https://geocoding-api.open-meteo.com/v1"

    @tool(description="Get the city geolocation: latitude and longitude")
    def get_city_geolocation(self, city: Annotated[str, "The city name"]) -> CityGeolocation:
        """Returns the latitude and longitude of the city."""
        log_tool_call("get_city_geolocation", f"city={city}")

        response = requests.get(f"{self.geolocationApiBaseUrl}/search?name={city}&count=1&language=en")        
        if response.status_code != 200:
            return f"Error: Unable to fetch geolocation data. Status code: {response.status_code}"
        
        data = response.json()
        
        if 'results' not in data or len(data['results']) == 0:
            return f"Error: No location found for city: {city}"
        
        location = data['results'][0]
        result = Result(
            name=location['name'],
            latitude=location['latitude'],
            longitude=location['longitude'],
            timezone=location.get('timezone', None)
        )
        
        search_result = SearchResult(results=[result])
        
        return CityGeolocation(search_result)

    @tool(description="Get current weather for a given latitude and longitude")
    def get_current_weather(self, latitude: Annotated[float, "Latitude"], 
                           longitude: Annotated[float, "Longitude"]) -> str:
        """Returns current weather data for the given coordinates."""
        log_tool_call("get_current_weather", f"latitude={latitude}, longitude={longitude}")

        response = requests.get(f"{self.apiUrlBase}/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        
        if response.status_code != 200:
            return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
        
        data = response.json()
        
        if 'current_weather' not in data:
            return "Error: Weather data not available for the specified location."
        
        current_weather = data['current_weather']
        result_str = f"Temperature: {current_weather['temperature']}°C, " \
                     f"Windspeed: {current_weather['windspeed']} km/h, " \
                     f"Wind direction: {current_weather['winddirection']}°, " \
                     f"Weather code: {current_weather['weathercode']}"
        
        return result_str