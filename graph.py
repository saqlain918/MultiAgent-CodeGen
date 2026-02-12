from langgraph.graph import StateGraph, END
from state import AgentState

from agents.manager import manager_agent
from agents.architecture import architecture_agent
from agents.code_writer import code_writer_agent
from agents.documentation import documentation_agent
from agents.file_saver import file_saver_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("manager", manager_agent)
    graph.add_node("architecture", architecture_agent)
    graph.add_node("code", code_writer_agent)
    graph.add_node("documentation", documentation_agent)
    graph.add_node("file_saver", file_saver_agent)

    graph.set_entry_point("manager")

    graph.add_conditional_edges(
        "manager",
        lambda s: s["mode"],
        {
            "full_project": "architecture",
            "architecture": "architecture",
            "code": "code",
            "documentation": "documentation",
            "explanation": "documentation"
        }
    )

    graph.add_edge("architecture", "code")
    graph.add_edge("code", "documentation")
    graph.add_edge("documentation", "file_saver")
    graph.add_edge("file_saver", END)

    graph.add_edge("architecture", END)
    graph.add_edge("code", END)
    graph.add_edge("documentation", END)

    return graph.compile()
