# Ollama

## Commands

```sh
  serve       Start Ollama
  create      Create a model
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  signin      Sign in to ollama.com
  signout     Sign out from ollama.com
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  launch      Launch the Ollama menu or an integration
  help        Help about any command
```

- list | ``ollama list``: show the list of downloaded models
- search
- pull | ``ollama pull <model>``: download the 
- run | ``ollama run <model>``: 
  - ``run <model> Hello world! --verbose`` return analysin and _tokens/s_
- show  ``ollama show <model>``


## Custom folder for models

Environment variable:
```sh 
OLLAMA_MODELS=E:\Ollama models
```

Shell:
```bash
export OLLAMA_MODELS="C:/path/to/your/custom/directory"
```



## Model context


``cd /e/Ollama\ models`` 
 mv phi3-mini-4k.Modelfile /e/Ollama\ models/


ollama show phi3:mini --modelfile > phi3-mini-4k.Modelfile

ollama create phi3-mini-4k -f phi3-mini-4k.Modelfile


## Create a fast version of "llama3.2"

``ollama run llama3.2 "Hello world" --verbose``

GT 710 1GB or RX 470 4GB:  
```sh       
total duration:       1.2567023s
load duration:        199.3381ms
prompt eval count:    27 token(s)
prompt eval duration: 117.4228ms
prompt eval rate:     229.94 tokens/s
eval count:           25 token(s)
eval duration:        927.275ms
eval rate:            26.96 tokens/s
```

GT 1070 8GB:  
```sh
total duration:       453.6389ms
load duration:        213.6126ms
prompt eval count:    27 token(s)
prompt eval duration: 20.9151ms
prompt eval rate:     1290.93 tokens/s
eval count:           10 token(s)
eval duration:        210.6521ms
eval rate:            47.47 tokens/s
```




## Models

[Models.md](Models.md)



## Thinking


The "thinking" feature can be disabled.  

# Disable thinking when running:
``ollama run espanol-profesora --think=false``

# Or use the interactive command inside a chat:
>>> /set nothink

# API call:
from ollama import chat

response = chat(
    model='espanol-profesora',
    messages=[{'role': 'user', 'content': 'Hola'}],
    think=False  # ← Disable thinking
)
print(response['message']['content'])


## TO READ

- https://www.reddit.com/r/ollama/comments/1rps0ux/my_local_setup_for_agentic_sessions_with_ollama/