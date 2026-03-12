module openAIClientBuilder

/// Helper for create OpenAI Client
type OpenAIClientBuilder (apiKey:string) =

    /// Create a OpenAIClient
    member this.BuildClient() =
        OpenAI.OpenAIClient(apiKey)

    /// Create a OpenAI Chat Client
    static member BuildChatClient(apiKey:string, model:string) =
        let client = OpenAI.OpenAIClient(apiKey)
        client.GetChatClient(model)
