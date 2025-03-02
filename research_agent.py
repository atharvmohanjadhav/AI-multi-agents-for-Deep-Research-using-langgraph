from langchain.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_result(query):
    search = TavilySearchResults(api_key = TAVILY_API_KEY)
    result = search.run(query,num_results = 5)
    return result

