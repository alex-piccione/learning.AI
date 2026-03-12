namespace Tools.Weather

open System.Threading.Tasks
open System.ComponentModel
open System.Net.Http
open Models.OpenMeteo
open System.Reflection
open Microsoft.Extensions.AI
open Microsoft.Extensions.Logging

open tools.toolsBase


[<Description("Coordinates of a city")>]
type CityLocation = {
    [<Description("The name of the city")>]
    City: string

    [<Description("The latitude coordinate")>]
    Latitude: float

    [<Description("The longitude coordinate")>]
    Longitude: float
}

type WeatherTools (logger:ILogger) =
    inherit ToolsBase()

    let client = new HttpClient()
    static let apiUrlBase = "https://api.open-meteo.com/v1"
    static let geolocationApiBaseUrl = "https://geocoding-api.open-meteo.com/v1"

    member private __.ProcessResponse<'T> (response:HttpResponseMessage) : Task<Result<'T, string>> = task {
        try
            let! content = response.Content.ReadAsStringAsync()
            if response.IsSuccessStatusCode then
                return Ok(deserialize<'T> content)
            else
                return Error($"{response.StatusCode} - {response.ReasonPhrase}. Content: {content}")
        with exn -> return Error($"Error processing response: {exn.Message}")
    }

    [<Description("Get the city geolocation: latitude and longitude")>]
    member __.GetCityGeolocation([<Description("The city name")>]city: string)
        : Task<CityLocation> = task {
        let url = $"{geolocationApiBaseUrl}/search?name={city}&count=1&language=en"
        try 
            let! response = client.GetAsync(url)
            //return! __.ProcessResponse<GetCityGeolocation>(response)
            match! __.ProcessResponse<geolocation.SearchResult>(response) with
            | Error err -> return failwith $"API error. {err}"
            | Ok searchResult ->
                if searchResult.results.Length > 0 then
                    let result = searchResult.results[0]
                    return {
                        City = result.name
                        Latitude = result.latitude
                        Longitude = result.longitude
                    }
                else
                    return failwith $"No geolocation found for city: {city}"
            
        with exn -> 
            logger.LogError(exn, "Error calling geolocation API")
            return failwith $"Error calling geolocation API: {exn.Message}"
        }


    (*
    fail: ConsoleApp[0]
    Error calling current weather forecast
    System.Exception: API error. Error processing response: Failed to deserialize response. Error: {"latitude":43.9,"longitude":12.919998,"generationtime_ms":0.10275840759277344,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":9.0,"current_units":{"time":"iso8601","interval":"seconds","temperature_2m":"°C","apparent_temperature":"°C","relative_humidity_2m":"%","rain":"mm","weather_code":"wmo code"},"current":{"time":"2026-03-12T16:45","interval":900,"temperature_2m":14.6,"apparent_temperature":13.5,"relative_humidity_2m":75,"rain":0.00,"weather_code":3}}. JSON: The JSON value could not be converted to System.DateTime[]. Path: $.current.time | LineNumber: 0 | BytePositionInLine: 374.
       at <StartupCode$Library>.$OpenMeteoTools.GetCurrentWeatherValues@70.MoveNext() in D:\Programming\AI\learning.AI\Microsoft Agent Framework .net\Library\Tools\OpenMeteoTools.fs:line 77
    *)

    [<Description("Get current weather forecast")>]
    member __.GetCurrentWeatherValues([<Description("The latitude")>]latitude: float, [<Description("The longitude")>]longitude: float)
        : Task<string> = task {
            let lat = latitude.ToString(System.Globalization.CultureInfo.InvariantCulture)
            let lon = longitude.ToString(System.Globalization.CultureInfo.InvariantCulture)
            let url = $"{apiUrlBase}/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,apparent_temperature,relative_humidity_2m,rain,weather_code"
            try
                let! response = client.GetAsync(url)
                match! __.ProcessResponse<forecast.Response>(response) with
                | Error err -> return failwith $"API error. {err}"
                | Ok result ->
                    return $"{result}"
                    //return {
                    //    City = result.hourly
                    //}
            
            with exn -> 
                logger.LogError(exn, "Error calling current weather forecast")
                return failwith $"Error calling current weather forecast: {exn.Message}"
        }

    (*
    member __.CreateTools () =
        let tools =
            __.GetType().GetMethods(BindingFlags.Public ||| BindingFlags.Instance)
            |> Seq.choose (fun m ->
                // Only pick methods that have a Description attribute
                let attr = m.GetCustomAttribute<DescriptionAttribute>()
                if isNull attr then None
                else
                    // Create the AIFunction and upcast to AITool
                    Some (AIFunctionFactory.Create(m, __) :> AITool)
            )
        System.Collections.Generic.List<AITool>(tools) // AIClient requires an IList<AITool>
        *) 

        //|> ResizeArray // Converts to the required IList<AITool>

        (*
    [<Description>]
    static member GetGeolocationFromCity (city: string) : string =

        let geocodeCity city =
            http {
                GET $"{apiUrlBase}/v1/search?name=%s{city}&count=1"
                Accept "application/json"
            }
            |> Request.send
            |> Response.toJson // parseJson<{| results: GeoResult array |}>
            |> fun json ->
                let lat = json?results?[0]?latitude.AsValue().GetSingle()
                let lon = json?results?[0]?longitude.AsValue().GetSingle()
                let name = json?results?[0]?name.GetString()

    [<Description>]
    member _.GetWeather(location: string) : string =
        // In a real implementation, this method would call a weather API to get the current weather for the specified location.
        // For this example, we'll return a hardcoded response.
        (*"""
        https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
        	"latitude": 52.52,
        	"longitude": 13.41,
        	"hourly": "temperature_2m",
        }
        """
        *)
        $"The current weather in {location} is sunny with a temperature of 25°C."

        *)