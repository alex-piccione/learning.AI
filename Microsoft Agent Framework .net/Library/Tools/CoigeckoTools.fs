module Tools.Coingecko

open System.ComponentModel
open Tools.ToolsBase
open Services.Coingecko
open Alex75.Cryptocurrencies
open Microsoft.Extensions.Logging

type CoingeckoTools (logger: ILogger, apiKey: string) =
    inherit ToolsBase()

    let client = CoingeckoClientDemo(apiKey)

    [<Description("Retrieve the price of the currency pair main/quote. It uses Coingecko Demo API.")>]
    member this.GetRate(main:string, quote:string) = task {
        logger.LogDebug($"{this.GetType().Name} | Call to GetRate | Start")
        return client.GetSinglePairRateAsync(Currency(main), Currency(quote))
    }

