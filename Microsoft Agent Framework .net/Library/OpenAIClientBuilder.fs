module OpenAIClientBuilder

open System
open Microsoft.Extensions.AI

/// Helper for create OpenAI Client
type OpenAIClientBuilder () =

    /// Create a OpenAI Chat Client
    static member BuildOpenAIChatClient(apiKey:string, model:string) =
        //OpenAI.OpenAIClient(apiKey)
        //    .GetChatClient(model)
        OpenAI.Chat.ChatClient(model, apiKey).AsIChatClient()
            

    static member BuildLocalOllamaChatClient(model:string) =
        let credentials = ClientModel.ApiKeyCredential "not required"
        let options = OpenAI.OpenAIClientOptions()
        options.Endpoint <- Uri "http://localhost:11434"
        //OpenAI.OpenAIClient(credentials, options)
        //    .GetChatClient(model)
        OpenAI.Chat.ChatClient(model, credentials, options).AsIChatClient()

    (*
    using Microsoft.Extensions.AI;
    
    IChatClient client =
        new OpenAI.Chat.ChatClient("gpt-4o-mini", Environment.GetEnvironmentVariable("OPENAI_API_KEY"))
        .AsIChatClient();
    
    Console.WriteLine(await client.GetResponseAsync(
    [
        new ChatMessage(ChatRole.System, "You are a helpful AI assistant"),
        new ChatMessage(ChatRole.User, "What is AI?"),
    ]));
    
    *)
