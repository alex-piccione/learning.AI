namespace Agents.Cryptocurrencies

open System.Threading
open Microsoft.Extensions.Logging
open Microsoft.Agents.AI
open Microsoft.Extensions.AI

open Tools.Kraken
open Tools.CoingeckoTools
open Tools.ToolsBase
open Tools.Wise

type CrytocurrenciesAgent (
    logger:ILogger,
    chatClient:OpenAI.Chat.ChatClient,
    krakenPublicKey:string,
    krakenPrivateKey:string,
    coingeckoApiKey:string,
    wiseApiKey:string
    ) =

    let name = "Cryptocurrencies Agent"
    let description = "Specialized agent for retrieving real-time price data, market trends, and exchange info via Kraken and Coingecko APIs."
    let instructions = """
    You are a professional Crypto Analyst. 
    Your goal is to provide accurate, real-time data using Kraken and Coingecko.

    Rules:
    1. If an API call fails, analyze the error (e.g., invalid ticker, rate limit) and explain it clearly to the user.
    2. Always specify which exchange/source the data is coming from.
    3. Use a concise, professional tone.
    """

    let krakenTools = KrakenTools(logger, krakenPublicKey, krakenPrivateKey).GetTools()

    let coingeckoTools = CoingeckoTools(logger, coingeckoApiKey).GetTools()

    let wiseTools = WiseTools(logger, wiseApiKey).GetTools()

    let tools = asList [krakenTools; coingeckoTools; wiseTools]
    
    let agent = chatClient.AsIChatClient().AsAIAgent(instructions, name, description, tools)
    let session = agent.CreateSessionAsync().AsTask() |> Async.AwaitTask |> Async.RunSynchronously

    member _.Ask (question:string, ct:CancellationToken) = task {
        let options:AgentRunOptions = AgentRunOptions()
        let! response = agent.RunAsync(question, session, options, ct)

        return response.ToString()
    }