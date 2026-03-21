# Models


| Model       | Params | VRAM     | Speed (t/s)  | Use Case              | Command                                  |
| --------    | ------ | ------   | ------------ | --------------------- | ---------------------------------------- |
| llama3.2:1b | 1B     | ~1.5GB   | ??           | Quick test            | ollama run llama3.2:1b                   |
| llama3.2    | 3B     | ~2GB     | 15-25        | Coding/chat (default) | ollama run llama3.2                      |
| phi3.2      | 3B     | ~2GB     | 20-30        | Fast assistant        | ollama run phi3.2                        |
| gemma2      | 2.6B   | ~1.8GB   | 20-35        | General               | ollama run gemma2:2b                     |
| qwen2.5     | 3B     | ~2GB     | 18-28        | Multilingual          | ollama run qwen2.5:3b                    |
| DeepSeek    | 7B?*   | ~4GB+    | 8-15 partial | Advanced (swap?)      | ollama run deepseek-coder:7b *borderline |

| NAME                                      | SIZE      | Params | VRAM (real)   |  Speed (t/s) | Use Case                     |
|-------------------------------------------|-----------|--------|---------------|-------------|------------------------------|
| codellama:7b                              | 3.8 GB    | 7B     | ~8 GB         | ~20         | Code generation, completion  |
| codellama:7b-code                         | 3.8 GB    | 7B     | ~8 GB         | ~20         | Code-focused tasks           |
| deepseek-r1:1.5b                          | 1.1 GB    | 1.5B   | ~3 GB         | ~40         | Lightweight code/model tasks |
| dolphin-llama3:8b                         | 4.7 GB    | 8B     | ~10 GB  5.2GB | ~25         | General chat, uncensored     |
| espanol-profesora-1:latest                | 2.0 GB    | ~1.5B  | ~3 GB         | ~35         | Spanish language tasks       |
| gemma:2b                                  | 1.7 GB    | 2B     | ~4 GB         | ~50         | Lightweight general use      |
| gemma:7b                                  | 5.0 GB    | 7B     | ~8 GB         | ~30         | General-purpose              |
| gemma3:1b                                 | 815 MB    | 1B     | ~2 GB         | ~60         | Fast, lightweight tasks      |
| hf.co/LEONW24/Qwen3.5-9B-Uncensored:Q4_K_M| 6.7 GB    | 9B     | ~12 GB        | ~15         | Uncensored chat, creativity  |
| hf.co/MaxedOut/ComfyUI-Starter-Packs:Q5_K_M| 3.4 GB   | -      | -        | -           | ComfyUI workflows            |
| hf.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF:Q4_K_S | 4.7 GB | 8B | ~10 GB | ~22 | General chat, uncensored |
| llama3.1:8b                               | 4.9 GB    | 8B     | ~10 GB   | ~25         | General chat, reasoning      |
| llama3.2:1b                               | 1.3 GB    | 1B     | ~2 GB    | ~70         | Fast, lightweight tasks      |
| llama3.2:3b                               | 2.0 GB    | 3B     | ~4 GB    | ~45         | Balanced performance         |
| llama3.2:latest                           | 2.0 GB    | 3B     | ~4 GB    | ~45         | General-purpose              |
| minimax-m2.7:cloud                        | -         | -      | -        | -           | Cloud-based model            |
| nomic-embed-text:latest                   | 274 MB    | -      | ~1 GB    | -           | Text embeddings              |
| phi3-mini-4k-fast:latest                  | 2.2 GB    | 3.8B   | ~4 GB    | ~40         | Fast inference, chat         |
| phi3-mini-4k:latest                       | 2.2 GB    | 3.8B   | ~4 GB    | ~35         | General chat, compact        |
| phi3.5:3.8b                               | 2.2 GB    | 3.8B   | ~5 GB    | ~30         | High efficiency, chat        |
| phi3:latest                               | 2.2 GB    | 3.8B   | ~4 GB    | ~35         | Lightweight general use      |
| qwen2.5-coder:1.5b-base                   | 986 MB    | 1.5B   | ~3 GB    | ~45         | Code-focused tasks           |
| qwen2.5-coder:7b                          | 4.7 GB    | 7B     | ~9 GB    | ~20         | Code generation              |
| qwen3.5:0.8b                              | 1.0 GB    | 0.8B   | ~2 GB    | ~80         | Ultra-lightweight tasks      |
| qwen3.5:2b                                | 2.7 GB    | 2B     | ~4 GB    | ~50         | Lightweight general use      |
| qwen3.5:4b                                | 3.4 GB    | 4B     | ~6 GB    | ~35         | Balanced chat/reasoning      |
| qwen3:1.7b                                | 1.4 GB    | 1.7B   | ~3 GB    | ~55         | Lightweight chat             |
| qwen3:latest                              | 5.2 GB    | 8B     | ~10 GB   | ~25         | General-purpose              |
| starcoder2:3b                             | 1.7 GB    | 3B     | ~4 GB    | ~40         | Code generation              |
| yi-coder:1.5b                             | 866 MB    | 1.5B   | ~3 GB    | ~50         | Lightweight code tasks       |"



## ollama run llama3.2-vision




## Dolphin 2.9 Llama 3 8b 🐬

https://huggingface.co/dphn/dolphin-2.9-llama3-8b

Dolphin-2.9 has a variety of instruction, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. I have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.



# https://huggingface.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF

``ollama run hf.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF:QUANT_TAG``
$ ollama run hf.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF:QUANT_TAG
pulling manifest
Error: pull model manifest: 400: {"error":"The specified tag is not a valid quantization scheme. Please use another tag or \"latest\""}



hf.co/Undi95/Mistral-11B-CC-Air-GGUF:Q4_K_M

seems completely rubbish