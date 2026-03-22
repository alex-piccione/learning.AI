module Settings

type AIService =
    | OpenAI
    | LocalOllama


let service = AIService.OpenAI

