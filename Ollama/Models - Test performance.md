# Models Perfo8rmance tests

$ ollama run dolphin-llama3:8b  "hello world" --verbose
$ ollama run dolphin-llama3:8b  "Small python function to sum 2 numbers" --verbose


model=hf.co/LEONW24/Qwen3.5-9B-Uncensored:Q4_K_M
ollama run $model "hello world" --verbose

## GT 1070 8GB


| Model                                                | tokens/s | RAM (GB) | CPU/GPU  | When    |
| -----------------------------------------------------|----------|----------|----------|---------| 
| dolphin-llama3:8b                                    | 45       | 5.2      | 100% GPU | 2026-03 |
| hf.co/LEONW24/Qwen3.5-9B-Uncensored:Q4_K_M           | 12       | 8.9      | 28%/72%  | 2026-03 |
| hf.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF:Q4_K_S | 37       | 5.2      | 100% GPU | 2026-03 |  
| hf.co/MaxedOut/ComfyUI-Starter-Packs:Q5_K_M          | 70       | 141MB    | 100% GPU | 2026-03 | 
| nemotron-3-nano:4b-q8_0                              | 
| qwen3.5:4b                                           | 20       | 5.9      | 100% GPU | 2026-03 | 


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