# Custom context

It is possible to create customization of the context.  
Given a model is possible to use a **Modelfile** to change some parameters and add a context.  




## Spanish teacher based on gemma:7b

```bash
cd /e/Ollama\ models
ollama show gemma:7b --modelfile > espanol-profesora.gemma:7b.1
code espanol-profesora.gemma:7b.1
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
