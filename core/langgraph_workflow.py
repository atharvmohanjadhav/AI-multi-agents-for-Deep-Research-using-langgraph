from agents.data_storing_agent import process_and_store
from agents.research_agent import search_result
from langgraph.graph import Graph,StateGraph
from langchain.schema import Document
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, END
from langchain.schema import Document

# Define state schema
class GraphState(TypedDict):
    question: str
    search_results: Annotated[Sequence[dict], operator.add]
    documents: Annotated[Sequence[Document], operator.add]
    vector_db: None
    final_answer: str

# Initialize graph
workflow = StateGraph(GraphState)

# Define nodes
def search_node(state: GraphState):
    question = state["question"]
    return {"search_results": search_result(question)}

def process_store_node(state: GraphState):
    final_res = [Document(page_content=item["content"]) for item in state["search_results"]]
    vector_db = process_and_store(final_res)
    return {"documents": final_res, "vector_db": vector_db}

def retrieve_node(state: GraphState):
    question = state["question"]
    vector_db = state["vector_db"]
    return {"documents": vector_db.similarity_search(question, k=2)}

def generate_answer_node(state: GraphState):
    question = state["question"]
    docs = state["documents"]
    response = chain.run(input_documents=docs, question=question)
    return {"final_answer": response}

# Add nodes
workflow.add_node("search", search_node)
workflow.add_node("process_store", process_store_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_answer_node)

# Set edges
workflow.set_entry_point("search")
workflow.add_edge("search", "process_store")
workflow.add_edge("process_store", "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)


