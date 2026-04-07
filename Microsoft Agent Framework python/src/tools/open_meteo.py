from agent_framework import tool
from typing import Annotated
import requests
import logging
from logging_configuration import log_tool_call
from rich import print

from .models.open_meteo_api import GeolocationSearchResult, GeolocationResult
from .models.open_meteo_output import CityGeolocation, CurrentWeather
from .models.json_helper import parse_json

# OpenMeteo documentation: https://open-meteo.com/en/docs


class OpenMeteoTools:

    apiUrlBase = "https://api.open-meteo.com/v1"
    geolocationApiBaseUrl = "https://geocoding-api.open-meteo.com/v1"

    def get_tools(self) -> list:
        return [self.get_city_geolocation, self.get_current_weather]
    

    @tool(description="Get the city geolocation: latitude and longitude")
    def get_city_geolocation(self, city: Annotated[str, "The city name"]) -> CityGeolocation:
        """Returns the latitude and longitude of the city."""
        log_tool_call("get_city_geolocation", f"city={city}")

        response = requests.get(f"{self.geolocationApiBaseUrl}/search?name={city}&count=1&language=en")        
        if response.status_code != 200:
            return f"Error: Unable to fetch geolocation data. Status code: {response.status_code}"
        
        data = response.json()
        logging.debug(data)
        
        if 'results' not in data or len(data['results']) == 0:
            return f"Error: No location found for city: {city}"
        
        """
        try
            # take the first result
            location = data['results'][0]
            result = GeolocationResult(
                name=location['name'],
                latitude=location['latitude'],
                longitude=location['longitude'],
                timezone=location['timezone']
                country=location["country"]
                country_code=location["country_code"]
            )
            
            search_result = GeolocationSearchResult(results=[result])
        """
        try:
            # take the first result
            result = data['results'][0]
       
            geolocation_result = parse_json(result, GeolocationResult)

            return CityGeolocation(
                name=geolocation_result.name,
                latitude=geolocation_result.latitude,
                longitude=geolocation_result.longitude
            )
        except Exception as ex:
            logging.error(f"Failed to parse response. {ex}. Response: {data}")
            raise Exception(f"Failed to parse response. {ex}")

            

    @tool(description="Get current weather for a given latitude and longitude")
    def get_current_weather(self, latitude: Annotated[float, "Latitude"], 
                           longitude: Annotated[float, "Longitude"]) -> CurrentWeather:
        """Returns current weather data for the given coordinates."""
        log_tool_call("get_current_weather", f"latitude={latitude}, longitude={longitude}")

        # f"{apiUrlBase}/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,apparent_temperature,relative_humidity_2m,rain,weather_code"
        response = requests.get(f"{self.apiUrlBase}/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        
        if response.status_code != 200:
            raise Exception(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        
        data = response.json()

        #print(data)
        #logging.info(f"Response: {data}")
        
        if 'current_weather' not in data:
            raise Exception("Error: Weather data not available for the specified location.")
        
        current_weather = data['current_weather']
        
        return CurrentWeather(
            temperature=current_weather['temperature'],
            wind_speed=current_weather['windspeed'],
            wind_direction= get_wind_direction(current_weather['winddirection']),
            weather_description=get_weather_description(current_weather['weathercode'])
        )
