# Models Perfo8rmance tests

$ ollama run dolphin-llama3:8b  "hello world" --verbose
$ ollama run dolphin-llama3:8b  "Small python function to sum 2 numbers" --verbose


model=hf.co/LEONW24/Qwen3.5-9B-Uncensored:Q4_K_M
ollama run $model "hello world" --verbose

## GT 1070 8GB

| Model                                                | Quantiz. | RAM (GB) | tokens/s | CPU/GPU  | When    |
| -----------------------------------------------------|----------|----------|----------|----------|---------|
| dolphin-llama3:8b                                    |          | 5.2      | 45       | 100% GPU  | 2026-03 | ✅
| hf.co/LEONW24/Qwen3.5-9B-Uncensored:Q4_K_M           |          | 8.9      | 12       | 28%/72% 🌡️| 2026-03 |
| hf.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF:Q4_K_S |          | 5.2      | 37       | 100% GPU | 2026-03 |
| hf.co/MaxedOut/ComfyUI-Starter-Packs:Q5_K_M          |          | 141 MB   | 70       | 100% GPU | 2026-03 |
| nemotron-3-nano:4b-q8_0                              |          | 6.6      | 35       | 100% GPU | 2026-03 |
| qwen3.5:4b                                           |          | 5.9      | 23       | 100% GPU | 2026-03 | ✅
| qwen3.5:2b                                           | Q8_0     | 4.2      | 28  🌡️    | 100% GPU | 2026-03 | ✅
| deepseek-r1:7b                                       | Q4_K_M   | 4.9      | 33       | 100% GPU | 2026-03 | qwen2 architecture
| deepseek-r1:8b                                       | Q4_K_M   | 6.0      | 29       | 100% GPU | 2026-03 | qwen3 architecture

$ ollama run dolphin-llama3:8b  "hello world" --verbose
Hi there! It's great to see you.

total duration:       14.2569336s
load duration:        13.7356176s
prompt eval count:    25 token(s)
prompt eval duration: 207.8657ms
prompt eval rate:     120.27 tokens/s
eval count:           11 token(s)
eval duration:        240.6482ms
eval rate:            45.71 tokens/s