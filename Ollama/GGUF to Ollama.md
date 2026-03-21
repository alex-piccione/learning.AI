# GGUF to Ollama

**NOT POSSIBLE WITH OLD HARDWARE**
Stop trying with ASUS Z77 and GTX 1070.  


1. Dowload the GGUF file (.gguf)   

2. Create a _Modelfile_ file and add this text to it:
```sh
FROM ./<file>.gguf
```

3. Add thsi commands to customize it (optional)

```sh
TEMPLATE: Defines the prompt structure (e.g., Instruction/Response).

PARAMETER: Sets values like num_ctx (context window) or temperature.

SYSTEM: Sets a persistent "personality" or role for the AI.
```

4. Run this command: ``ollama create <model> -f Modelfile

