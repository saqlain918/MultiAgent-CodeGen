from config import llm

def documentation_agent(state):
    prompt = f"""
Write README documentation.

Architecture:
{state.get("architecture", "")}

Files:
{list(state.get("files", {}).keys())}
"""
    state["documentation"] = llm.invoke(prompt).content
    return state
