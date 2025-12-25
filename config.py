from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

def get_llm(api_key: str):
    return ChatGroq(
        groq_api_key = api_key,
        model_name = "llama-3.3-70b-versatile",
        temperature= 0.5,
        streaming = True
    )

def get_embeddings():
    return HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2") 