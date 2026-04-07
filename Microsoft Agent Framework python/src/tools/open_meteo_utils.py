def get_wind_direction(direction_degrees) -> str:
    """Returns the wind direction as Nort"""
    # < 22.5 or  -> north
    # < 67.5 -> north-east
    # < 112.5 -> east
    # ...
    # > 337.5 -> north

    if (direction_degrees > 315 or direction_degrees < 45):
        return "north"
    elif (direction_degrees > 90):

def get_weather_code_description(code: int) -> str:
    """
    Returns the description for a given WMO (World Meteorological Organization) weather code.
    
    Args:
        code: The WMO weather code
        
    Returns:
        Description of the weather condition
        
    Documentation: https://open-meteo.com/en/docs#weather_variable_documentation
    """
    if code == 0:
        return "Clear sky"
    elif code in [1, 2, 3]:
        return "Mainly clear, partly cloudy, and overcast"
    elif code in [45, 48]:
        return "Fog and depositing rime fog"
    elif code in [51, 53, 55]:
        return "Drizzle: Light, moderate, and dense intensity"
    elif code in [56, 57]:
        return "Freezing Drizzle: Light and dense intensity"
    elif code in [61, 63, 65]:
        return "Rain: Slight, moderate and heavy intensity"
    elif code in [66, 67]:
        return "Freezing Rain: Light and heavy intensity"
    elif code in [71, 73, 75]:
        return "Snow fall: Slight, moderate, and heavy intensity"
    elif code == 77:
        return "Snow grains"
    elif code in [80, 81, 82]:
        return "Rain showers: Slight, moderate, and violent"
    elif code in [85, 86]:
        return "Snow showers: slight and heavy"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    elif code in [96, 99]:
        return "Thunderstorm with slight and heavy hail"
    else:
        return f"Unknown weather code: {code}"