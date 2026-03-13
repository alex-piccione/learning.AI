module Tools.CoingeckoTools

open System.ComponentModel
open System.Threading.Tasks
open Microsoft.Extensions.Logging
open Alex75.Cryptocurrencies.Services.Coingecko
open Alex75.Cryptocurrencies

open Tools.ToolsBase
open Tools.Coingecko.Models

type CoingeckoTools (logger: ILogger, apiKey: string) =
    inherit ToolsBase()

    let client = CoingeckoClientDemo(apiKey)

    [<Description("Retrieve the price (exhange rate) of the currency pair main/quote. It uses Coingecko Demo API.")>]
    member this.GetRate(main:string, quote:string) : Task<decimal> = 
        logger.LogDebug($"{this.GetType().Name} | Call to GetRate | Start")
        client.GetSinglePairRateAsync(CurrencyPair(main, quote))
    

    [<Description("Retrieve the price (exhange rate) of the currency pairs provided. It uses Coingecko Demo API.")>]
    member this.GetRates(mains:string seq, quotes:string seq) : Task<CurrencyPairRate list>  = task {
        logger.LogDebug($"{this.GetType().Name} | Call to GetRates | Start")

        let! apiResult = (client.GetPairsRateAsync(
            mains   |> Seq.map (fun m -> Currency(m)),
            quotes  |> Seq.map (fun q -> Currency(q))
        ))

        return CurrencyPairRate.fromApiResponse apiResult
    }