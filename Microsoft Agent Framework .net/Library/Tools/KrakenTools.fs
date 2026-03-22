module Tools.Kraken

open Microsoft.Extensions.Logging
open System.ComponentModel
open Alex75.KrakenApiClient
open ToolsBase

type KrakenTools (logger:ILogger, krakenPublicKey, kakenSecretKey) =
    inherit ToolsBase()

    let client = Client(krakenPublicKey, kakenSecretKey) :> IClient

    [<Description("Retrieve the balances of the owned currencies (crypto and fiat) in the Kraken exchange")>]
    member this.GetBalance () = task {
        logger.LogInformation($"{this.GetType().Name} | Call to GetBalance | Start")
        try 
            let! balance = client.GetBalance()
            logger.LogInformation($"{this.GetType().Name} | Call to GetBalance | Success")
            return balance
            
        with ex -> 
            logger.LogError($"{this.GetType().Name} | Call to GetBalance | Failed. {ex}")
            return failwith $"Failed to call Kraken API. {ex}"
    }