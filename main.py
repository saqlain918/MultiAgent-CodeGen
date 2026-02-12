from graph import build_graph

def main():
    app = build_graph()

    print("\n🧠 Multi-Agent Coding System (Terminal)")
    print("Type what you want to build\n")

    user_input = input("👉 ")

    result = app.invoke({
        "user_input": user_input,
        "mode": "",
        "plan": "",
        "architecture": "",
        "files": {},
        "documentation": "",
        "response": ""
    })

    print("\n" + result.get("response", "Done"))

if __name__ == "__main__":
    main()
