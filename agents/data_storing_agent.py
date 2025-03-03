
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from agents.research_agent import search_result
from langchain.schema import Document

def process_and_store(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(data)
    load_dotenv()

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")

    pinecone_client = pinecone.Pinecone(api_key=PINECONE_API_KEY)

    index = pinecone_client.Index(PINECONE_INDEX)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    from langchain.vectorstores import Pinecone
    vector_db = Pinecone.from_documents(documents, embedding=embeddings, index_name=PINECONE_INDEX)

    return vector_db
res = search_result("trending sports news?")

final_res = []
for i in res:
    final_res.append(Document(i['content']))
process_and_store(final_res)
