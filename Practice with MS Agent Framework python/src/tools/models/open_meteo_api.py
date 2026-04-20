from dataclasses import dataclass
from typing import List, Annotated
from datetime import datetime


@dataclass
class GeolocationResult:      
    name: str
    latitude: float
    longitude: float
    elevation: float
    population: int
    country_code: str
    country: str
    timezone: str


@dataclass
class GeolocationSearchResult: 
    results: List[GeolocationResult]


@dataclass
class ForecastCurrentData:
    """Current weather data."""
    time: Annotated[datetime, "Time of the measurement"]
    temperature_2m: Annotated[float, "Air temperature at 2 meters above ground. °C (Celsius)."]
    relative_humidity_2m: Annotated[float, "Relative humidity at 2 meters above ground. °C (Celsius)."]
    apparent_temperature: Annotated[float, "Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation"]
    precipitation: Annotated[float, "Total precipitation (rain, showers, snow) sum of the preceding hour. mm (millimeters)."]
    rain: Annotated[float, "Rain from large scale weather systems of the preceding hour in millimeter."]
    precipitation_probability: Annotated[float, "Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution."]
    wind_speed_10m: Annotated[float, "Wind speed (Km/h) at 10 meters above ground."]
    cloud_cover: Annotated[float, "Total cloud cover as an area fraction."]


@dataclass
class ForecastHourlyData:
    """Hourly weather forecast data."""
    time: List[Annotated[datetime, "Array of timestamps"]]
    temperature_2m: List[Annotated[float, "Air temperature at 2 meters above ground. °C (Celsius)."]]
    relative_humidity_2m: List[Annotated[float, "Relative humidity at 2 meters above ground. °C (Celsius)."]]
    apparent_temperature: List[Annotated[float, "Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation"]]
    precipitation: List[Annotated[float, "Total precipitation (rain, showers, snow) sum of the preceding hour. mm (millimeters)."]]
    rain: List[Annotated[float, "Rain from large scale weather systems of the preceding hour in millimeter."]]
    precipitation_probability: List[Annotated[float, "Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution."]]
    wind_speed_10m: List[Annotated[float, "Wind speed (Km/h) at 10 meters above ground."]]
    cloud_cover: List[Annotated[float, "Total cloud cover as an area fraction."]]


@dataclass
class ForecastResponse:
    """Forecast response containing current and hourly data."""
    current: Annotated[ForecastCurrentData, "A list of weather variables to get current conditions."]
    hourly: Annotated[ForecastHourlyData, "Hourly values"]