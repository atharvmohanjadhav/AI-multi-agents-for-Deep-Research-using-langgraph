import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from agents.data_storing_agent import process_and_store
from agents.research_agent import search_result
from dotenv import load_dotenv
from langchain.schema import Document
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
res = search_result("trending sports news?")

final_res = []
for i in res:
    final_res.append(Document(i['content']))
vector_db = process_and_store(final_res)
# Initialize Groq LLaMA model
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
chain = load_qa_chain(llm,chain_type="stuff")
def retrieve(query,k=2):
    res = vector_db.similarity_search(query=query,k = k)
    return res

def draft_answer(query):
    search = retrieve(query)
    print(search)
    response = chain.run(input_documents=search,question=query)
    return response

print(draft_answer("trending cricket news?"))