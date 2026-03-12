//namespace UnitTests.Tools.OpenMeteo
module unitTests.tools.OpenMeteo

(*
fail: ConsoleApp[0]
Error calling current weather forecast
System.Exception: API error. Error processing response: Failed to deserialize response. Error: {"latitude":43.9,"longitude":12.919998,"generationtime_ms":0.10275840759277344,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":9.0,"current_units":{"time":"iso8601","interval":"seconds","temperature_2m":"°C","apparent_temperature":"°C","relative_humidity_2m":"%","rain":"mm","weather_code":"wmo code"},"current":{"time":"2026-03-12T16:45","interval":900,"temperature_2m":14.6,"apparent_temperature":13.5,"relative_humidity_2m":75,"rain":0.00,"weather_code":3}}. JSON: The JSON value could not be converted to System.DateTime[]. Path: $.current.time | LineNumber: 0 | BytePositionInLine: 374.
   at <StartupCode$Library>.$OpenMeteoTools.GetCurrentWeatherValues@70.MoveNext() in D:\Programming\AI\learning.AI\Microsoft Agent Framework .net\Library\Tools\OpenMeteoTools.fs:line 77
*)


open NUnit.Framework

[<SetUp>]
let Setup () =
    ()

[<Test>]
let Test1 () =
    Assert.Pass()
