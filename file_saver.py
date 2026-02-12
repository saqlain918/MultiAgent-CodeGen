import os
import re

def file_saver_agent(state):
    project_name = re.sub(r"[^a-zA-Z0-9_]", "_", state["user_input"].lower())[:40]
    base_dir = f"workspace/{project_name}"

    os.makedirs(base_dir, exist_ok=True)

    for filename, content in state["files"].items():
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(state["documentation"])

    state["response"] = f"✅ Project created at {base_dir}"
    return state
