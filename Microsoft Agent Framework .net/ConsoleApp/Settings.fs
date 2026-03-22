module Settings

type AIService =
    | OpenAI
    | LocalOllama


let service = AIService.LocalOllama


(*
llama3.2:3b (2GB, excellent tool use, multilingual/agentic) – Best starter.
dolphin-llama3:8b (4.7GB, strong coding/tools, uncensored).
qwen3.5:4b or qwen3.5:2b (3.4GB/2.7GB, good multilingual/tools, but finicky—test first).
nemotron-3-nano:4b-q8_0 (4.2GB, solid tools).
*)

let OllamaModel = "nemotron-3-nano:4b-q8_0"