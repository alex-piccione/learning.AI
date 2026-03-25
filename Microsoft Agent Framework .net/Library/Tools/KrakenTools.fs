module Tools.Kraken

open Microsoft.Extensions.Logging
open System.ComponentModel
open Alex75.KrakenApiClient
open ToolsBase

type KrakenTools (logger:ILogger, krakenPublicKey, kakenSecretKey) =
    inherit ToolsBase(logger)

    let client = Client(krakenPublicKey, kakenSecretKey) :> IClient

    [<Description("Retrieve the balances of the owned currencies (crypto and fiat) in the Kraken exchange")>]
    member this.GetBalance () = task {
        this.LogCall "GetBalance" None
        try 
            let! balance = client.GetBalance()
            return balance

        with ex -> 
            this.LogError "GetBalance" ex
            return failwith $"Failed to call Kraken API. {ex}"
    }