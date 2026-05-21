from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from app.agents.researcher import research_agent
from app.agents.analyst import analyst_agent
from app.agents.writer import writer_agent
from app.agents.reviewer import reviewer_agent


class WorkflowState(TypedDict):
    task: str
    research: str
    analysis: str
    draft: str
    final_output: str


def build_graph():
    graph = StateGraph(WorkflowState)

    graph.add_node("researcher", research_agent)
    graph.add_node("analyst", analyst_agent)
    graph.add_node("writer", writer_agent)
    graph.add_node("reviewer", reviewer_agent)

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "analyst")
    graph.add_edge("analyst", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", END)

    return graph.compile()


workflow_app = build_graph()


def run_workflow(task: str):
    initial_state = {
        "task": task,
        "research": "",
        "analysis": "",
        "draft": "",
        "final_output": ""
    }

    return workflow_app.invoke(initial_state)