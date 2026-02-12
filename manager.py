from config import llm

def manager_agent(state):
    prompt = f"""
You are a coding task manager.

Classify the request into ONE mode:
- full_project
- architecture
- code
- documentation
- explanation

User request:
{state['user_input']}

Return ONLY the mode name.
"""
    state["mode"] = llm.invoke(prompt).content.strip().lower()
    return state
