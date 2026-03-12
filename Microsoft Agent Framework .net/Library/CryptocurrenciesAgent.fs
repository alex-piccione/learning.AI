namespace Agents.Cryptocurrencies

open System.Threading
open Microsoft.Extensions.Logging
open Microsoft.Agents.AI
open Microsoft.Extensions.AI

open Tools.Kraken

type CrytocurrenciesAgent (logger:ILogger, chatClient:OpenAI.Chat.ChatClient, krakenPublicKey:string, krakenPrivateKey:string) =

    let name = "Cryptocurrencies Agent"
    let instructions = """
        You are am expert about cryptocurrencies.
    """
    let description = """
        Retrieve info about the cryptocurrencies.
        When a call to some Ezcnage AI fails, explain the error.
    """

    let krakenTools = KrakenTools(logger, krakenPublicKey, krakenPrivateKey).GetTools()

    let tools = krakenTools
    let agent = chatClient.AsIChatClient().AsAIAgent(instructions, name, description, tools)
    let session = agent.CreateSessionAsync().AsTask() |> Async.AwaitTask |> Async.RunSynchronously

    member _.Ask (question:string, ct:CancellationToken) = task {
        let options:AgentRunOptions = AgentRunOptions()
        let! response = agent.RunAsync(question, session, options, ct)

        return response.ToString()
    }