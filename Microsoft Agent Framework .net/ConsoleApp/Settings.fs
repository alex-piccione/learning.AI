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

let OllamaModel
    //= "llama3.2:3b"
    = "llama3.1:8b"
    //= "nemotron-3-nano:4b-q8_0"
    //= "llama3-groq-tool-use"


(*

| Model                | Agent | Result | Note                                                            | 
|----------------------|-------|--------|-----------------------------------------------------------------|
| llama3.1:8b          | V1    | ❌     | No usage of Coingecko tool.                                     |
| llama3.2:3b          | V1    | ❌     | No usage of Coingecko tool.                                     |
| dolphin-llama3:8b    | V1    | ❌     | No usage of Coingecko tool. LIED about it ⚠️ (said it used it)  |
| llama3.1:8b          | V2    | ✅     | No usage of Coingecko tool. LIED about it ⚠️ (said it used it)  |



✅ or ✔️
❌ or ⚠️
🤖
🤔 or 🧠
💡
🎯 Target
⚙️ Settings
🛠️ Tools
*)