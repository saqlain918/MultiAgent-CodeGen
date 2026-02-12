from typing import TypedDict, Dict

class AgentState(TypedDict):
    user_input: str
    mode: str

    plan: str
    architecture: str
    files: Dict[str, str]
    documentation: str

    response: str
