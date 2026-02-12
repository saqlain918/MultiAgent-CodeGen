from config import llm

def architecture_agent(state):
    prompt = f"""
You are a software architect.

Design architecture for:
{state['user_input']}

Explain file structure and responsibilities.
"""
    state["architecture"] = llm.invoke(prompt).content
    return state
