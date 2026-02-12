from config import llm
import json
import re

# -----------------------------
# JSON extraction helper
# -----------------------------
def extract_json(response):
    """
    Extracts the first {...} block from the LLM response.
    This prevents JSONDecodeError if the LLM adds extra text.
    """
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError(f"No valid JSON found in LLM response:\n{response}")

# -----------------------------
# Code Writer Agent
# -----------------------------
def code_writer_agent(state):
    prompt = f"""
You are a senior developer.

Architecture:
{state.get("architecture", "")}

Generate ALL required code files.

Return STRICT JSON ONLY:
{{
  "files": {{
    "main.py": "...",
    "app.py": "..."
  }}
}}

Return ONLY JSON, no extra text or explanations.
"""
    response = llm.invoke(prompt).content

    # Safely extract JSON from the LLM response
    data = extract_json(response)

    # Save files in state
    state["files"] = data["files"]

    return state
