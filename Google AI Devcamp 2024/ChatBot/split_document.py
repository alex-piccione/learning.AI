import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

print(f"API KEY: {openai_api_key}")

if not openai_api_key:
    raise ValueError('OpenAI API keys not set. Please set it in the .env file.')

#text = "This is an example. Yo voy al mar la manana. come estas tu? Yo compra el pan. what is login of keychain alert in macbook?"

# Split the text
#text_splitter = RecursiveCharacterTextSplitter(
#    chunk_size=20,
#    chunk_overlap=10,
#    separators=["\n\n", "\n", " ", ""]
#)
#split_texts = text_splitter.split_text(text)

# # Print each split text chunk to the console to see the output
#for i, chunk in enumerate(split_texts):
#    print(f"Chunk {i+1}:")
#    print(chunk)
#    print("\n" + "-"*80 + "\n")  # Separator line between chunks for readability


try:
    # Read the file
    script_dir = os.path.dirname(__file__)
    print(f"PATH: {script_dir}")

    with open("gym_faqs.txt", "r", encoding="utf8") as file:
        text = file.read()

    # Split the text
    #text-embedding-ada-002
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,        
        separators=["\n\n", "\n", " ", ""]
    )
    split_texts = text_splitter.split_text(text)

    # # Print each split text chunk to the console to see the output
    for i, chunk in enumerate(split_texts):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("\n" + "-"*80 + "\n")  # Separator line between chunks for readability

    # Create document objects
    docs = [Document(page_content=chunk) for chunk in split_texts]
    
    # Initialize OpenAI embeddings
    model_for_text_embedding = "text-embedding-3-small" # default text-embedding-ada-002
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, model=model_for_text_embedding)

    # Initialize Chroma vector store
    persist_directory = "./chroma_db"
    vectorstore = Chroma.from_documents(docs, embedding=embeddings, persist_directory=persist_directory)

    print("Success!")
except Exception as e:
    print(f"An error occurred: {e}")
