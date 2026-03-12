module tools.kraken

open Microsoft.Extensions.Logging
open System.ComponentModel
open Alex75.KrakenApiClient
open toolsBase

type KrakenTools (logger:ILogger, krakenPublicKey, kakenSecretKey) =
    inherit ToolsBase()

    let client = Client(krakenPublicKey, kakenSecretKey) :> IClient

    [<Description("Retrieve the balances of the owned currencies (crypto and fiat) in the Kraken exchange")>]
    member this.GetBalance () =
        logger.LogDebug($"{this.GetType().Name} | Call to GetBalance")
        let balance = client.GetBalance()

        balance