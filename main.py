from core.langgraph_workflow import workflow
app = workflow.compile()

# Usage example
inputs = {"question": "trending cricket news?"}
result = app.invoke(inputs)
print(result["final_answer"])

result = app.invoke({"question": "trending cricket news?"})
print(result["final_answer"])
from IPython.display import Image, display
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles

import os

png_graph = app.get_graph().draw_mermaid_png()
with open("my_graph.png", "wb") as f:
    f.write(png_graph)

print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")