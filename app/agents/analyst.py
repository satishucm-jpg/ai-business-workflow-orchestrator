from app.config import llm

def analyst_agent(state):
    prompt = f"""
You are a Data Analyst Agent.

Based on the research below, provide:
1. Key insights
2. Risks
3. Opportunities
4. Business recommendation

Research:
{state["research"]}
"""

    response = llm.invoke(prompt)
    state["analysis"] = response.content
    return state