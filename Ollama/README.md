# Ollama

## Comamnds

`list`
`search`
`pull`
`run`
`run <model> Hello world! --verbose`  get tokens/s


## Model context

``cd /e/Ollama\ models`` 
 mv phi3-mini-4k.Modelfile /e/Ollama\ models/


ollama show phi3:mini --modelfile > phi3-mini-4k.Modelfile

ollama create phi3-mini-4k -f phi3-mini-4k.Modelfile


## Create a fast version of "llama3.2"
```sh
$ ollama run llama3.2 "Hello world" --verbose
Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?

total duration:       1.2567023s
load duration:        199.3381ms
prompt eval count:    27 token(s)
prompt eval duration: 117.4228ms
prompt eval rate:     229.94 tokens/s
eval count:           25 token(s)
eval duration:        927.275ms
eval rate:            26.96 tokens/s
```

```bash
cd /e/Ollama\ models
ollama show llama3.2 --modelfile > llama3.2-4k-fast.Modelfile
code  llama3.2-4k-fast.Modelfile
```


```bash
ollama create espanol-profesora-1  -f llama3.2-4k-fast.Modelfile
ollama list | grep espanol
ollama run espanol-profesora-1
``` 



## AMD RX 470 

Ollama on Windows uses ROCm, which officially only supports modern RX 6000/7000 cards. It sees your RX 470 as "too old" and ignores it.

You can set an Environment Variable:
``HSA_OVERRIDE_GFX_VERSION`` = ``8.0.3``

or use ``set`` or ``setx``:
```bash
set HSA_OVERRIDE_GFX_VERSION=8.0.3
```


Latest Ollama is capable to use Vulkan "driver". Vilkan driver can communicate with RX 470.  

You can set an Environment Variable:
``OLLAMA_VULKAN`` = ``1``

```bash
export OLLAMA_VULKAN=1
ollama serve
```






| Model       | Params | VRAM     | Speed (t/s)  | Use Case              | Command                                  |
| --------    | ------ | ------   | ------------ | --------------------- | ---------------------------------------- |
| llama3.2:1b | 1B     | ~1.5GB   | ??           | Quick test            | ollama run llama3.2:1b                   |
| llama3.2    | 3B     | ~2GB     | 15-25        | Coding/chat (default) | ollama run llama3.2                      |
| phi3.2      | 3B     | ~2GB     | 20-30        | Fast assistant        | ollama run phi3.2                        |
| gemma2      | 2.6B   | ~1.8GB   | 20-35        | General               | ollama run gemma2:2b                     |
| qwen2.5     | 3B     | ~2GB     | 18-28        | Multilingual          | ollama run qwen2.5:3b                    |
| DeepSeek    | 7B?*   | ~4GB+    | 8-15 partial | Advanced (swap?)      | ollama run deepseek-coder:7b *borderline |