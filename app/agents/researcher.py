from app.config import llm

def research_agent(state):
    task = state["task"]

    prompt = f"""
You are a Research Agent.

Research the following business task and provide:
1. Background context
2. Key facts
3. Market or business relevance
4. Important considerations

Task:
{task}
"""

    response = llm.invoke(prompt)
    state["research"] = response.content
    return state