# RAG Chatbot

This is an LLM Chatbot powered by RAG. The tech stack includes Python, Langchain, OpenAI and Chroma DB vector store. Hosted on Streamlit.

LLM - Large Language Model  
RAG - Retrieval Augumented Generation  

For a video walkthrough, [click this YouTube link to watch](https://youtube.com/playlist?list=PL4gEDuKXcNsMyegMNyhjVi-mqf0hvoIWu&si=hSJnQGZ4ubcXebwl).

![image info](./images/thumbnail.png)


1. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # for bash in Windows
source .venv/bin/activate  # for unix
```

2. Install libraries and dependencies
```bash
pip install -r requirements.txt
```

3. Get [OpenAI API key](https://platform.openai.com/account/api-keys)
and set it in _.env_ file
``OPENAI_API_KEY=sk-proj-tQHj********``

4. Run Streamlit app
```bash
streamlit run main.py
```

Split document and save to Supabase Vector database (Run once or only when you need to store a document)
```bash
python split_document.py
```

### More Docs and Links
[Streamlit Docs](https://docs.streamlit.io/get-started)  
[Langchain Python Docs](https://python.langchain.com/v0.2/docs/introduction/)  
[Langchain Conversational RAG Docs](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)  

