namespace Library

open Microsoft.Agents.AI
open Microsoft.Extensions.AI
open System.Threading

type WeatherAgent (agent: AIAgent) =

    let session = agent.CreateSessionAsync().AsTask() |> Async.AwaitTask |> Async.RunSynchronously

    static member CreateChatClientUsingOpenAI(apiKey:string, model:string) =

        let client = OpenAI.OpenAIClient(apiKey)
        let chatClient = client.GetChatClient(model)
        let agent = chatClient.AsIChatClient().AsAIAgent()
        WeatherAgent(agent)

        //Microsoft.Agents.AI.AIAgentBuilder.
        //let client = OpenAI.OpenAIClient()
        //let client = AzureOpenAIClient()

    member _.Ask (question:string, ct:CancellationToken) = async {
        let options:AgentRunOptions = AgentRunOptions()
        let! response = agent.RunAsync(question, session, options, ct) |> Async.AwaitTask

        //response.Text
        return response.ToString()
    }

        //let message = ChatMessage.FromUser(question)
        //let response = agent.GetResponseAsync([message]) |> Async.AwaitTask |> Async.RunSynchronously
        //response.Choices.[0].Message.Content)

    //let hello name =
    //    printfn "Hello %s" name