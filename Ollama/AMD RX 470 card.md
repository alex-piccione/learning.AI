# AMD RX 470 card

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
