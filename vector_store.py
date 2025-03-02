
import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from agents.research_agent import search_result

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
pinecone.init(api_key = PINECONE_API_KEY,environment="aped-4627-b74a")
pinecone_client = pinecone.Pinecone(api_key=PINECONE_API_KEY)

index = pinecone_client.Index(PINECONE_INDEX)
#print(pinecone_client.list_indexes())

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = Pinecone(index, embeddings.embed_query, PINECONE_INDEX)

res = search_result("trending articles on internet?")
