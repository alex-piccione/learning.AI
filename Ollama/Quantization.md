# Quantization


Q8_0  is ok

Q4 is what usually is used for Ollama models.

Q3 means 3 bits and is more compressed than Q4 (4 bits), so lower size and maybe faster but less quality.  
K_M and K_S are compressions, and reduces quality: Q4_0 is better than Q4_K_S.
Q4_K_S is better than Q4_K_M.  

  
Q3_K_S  
Q4_K_M  
Q4_K_S  

Q3_K_S  
Q4_K_M  
Q4_K_S  
  
bf16   ???