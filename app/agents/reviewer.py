from app.config import llm

def reviewer_agent(state):
    prompt = f"""
You are a Reviewer Agent.

Improve the draft below for:
1. Clarity
2. Professional tone
3. Structure
4. Completeness

Draft:
{state["draft"]}
"""

    response = llm.invoke(prompt)
    state["final_output"] = response.content
    return state