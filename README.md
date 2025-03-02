# AI-multi-agents-for-Deep-Research-using-langgraph

AI agent-based Deep Research
AI Research Chatbot Summary:
The AI-powered research chatbot follows a structured Langgraph workflow to generate research-based answers by integrating web search, vector-based retrieval, and LLM-powered response generation.
Workflow Breakdown:
1.	Research Agent: It fetches relevant information from the web using Tavily APIs. I created a search_result(query) function to fetch the latest news or research papers. It gives a list of search results containing text content.
2.	Data processing Agent: It stores and indexes the retrieved search data in a vector database for efficient retrieval. For that, I use a Pinecone vector database. In this, I convert the search results into document format and create a function process_and_store(data) to embed and store the data. As an output is a searchable vector database for future queries.
3.	Answer Drafting Agent: It retrieves the most relevant stored data and generates an answer using Groq’s LLaMA-3 model. It retrieves the top-k similar documents from the vector database and passes them to the LLM (ChatGroq) using a QA chain for response. It gives a well-structured response.
Implementation of Langghraph:
1.	First, I define the Graph
2.	Then add node:
•	Research Agent 
•	Data Processing Agent 
•	Answer Drafting Agent
3.	Then I define the edges to connect the nodes.
4.	Then I set an Entry Point & Compile the Workflow.

