module KrakenModels

open System.ComponentModel
open Alex75.Cryptocurrencies

type Ticker = {
    [<Description("Highest price offered for buy in the market")>]
    Bid: decimal
    [<Description("Lowest price offered for sell in the market")>]
    Ask: decimal
}

type Ticker with
    static member FromApiTicker (ticker:Alex75.Cryptocurrencies.Ticker): Ticker =
        {
            Bid = ticker.Bid
            Ask = ticker.Ask
        }
