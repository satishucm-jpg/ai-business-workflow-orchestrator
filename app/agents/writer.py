from app.config import llm

def writer_agent(state):
    prompt = f"""
You are a Professional Writer Agent.

Create a polished business email/report using the analysis below.

Analysis:
{state["analysis"]}
"""

    response = llm.invoke(prompt)
    state["draft"] = response.content
    return state