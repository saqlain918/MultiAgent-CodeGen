# 🤖 MultiAgent-CodeGen

## 📖 Overview

**MultiAgent-CodeGen** is an intelligent coding assistant powered by Google Gemini and LangChain that uses a multi-agent architecture to automatically generate complete Python projects from natural language descriptions. Simply describe what you want to build, and watch as specialized AI agents collaborate to design, code, and document your project.

### 🎯 What Makes It Special?

- **Zero Boilerplate** – No more starting from scratch
- **Intelligent Architecture** – AI-designed project structures
- **Production-Ready Code** – Clean, documented, and organized
- **Automatic Documentation** – Professional README files included
- **Multi-Agent Collaboration** – Specialized agents working together

---

## ✨ Features

### 🚀 Core Capabilities

- **Terminal-Driven Workflow** – Run everything directly from your command line
- **Multi-Agent System** – Coordinated agents handling different aspects of development
- **Dynamic Project Generation** – Create any Python project from natural language
- **Smart Workflow Routing** – Automatically determines full project, code-only, or docs-only modes
- **Automatic Documentation** – Generates comprehensive README.md files
- **Organized Workspace** – Clean project structure in dedicated `workspace/` directory

### 🤝 Agent Roles

| Agent | Responsibility |
|-------|---------------|
| **Manager** | Analyzes input and orchestrates workflow |
| **Architecture** | Designs project structure and file organization |
| **Code Writer** | Generates clean, functional Python code |
| **Documentation** | Creates professional documentation |
| **File Saver** | Manages file system operations |

---

## 🏗️ How It Works

```
graph LR
    A[User Input] --> B[Manager Agent]
    B --> C[Architecture Agent]
    C --> D[Code Writer Agent]
    D --> E[Documentation Agent]
    E --> F[File Saver Agent]
    F --> G[Generated Project]
```

### Step-by-Step Process

1. **📝 User Input** – Describe your project in natural language
2. **🎯 Manager Agent** – Analyzes requirements and determines workflow mode
3. **🏛️ Architecture Agent** – Designs project structure and defines file responsibilities
4. **💻 Code Writer Agent** – Generates Python code based on architectural plan
5. **📚 Documentation Agent** – Creates professional README and documentation
6. **💾 File Saver Agent** – Organizes and saves all files to workspace
7. **✅ Output** – Terminal displays path to your complete project

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Git (for cloning)

### Quick Start

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/MultiAgent-CodeGen.git
cd MultiAgent-CodeGen
```

#### 2️⃣ Create Virtual Environment

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

#### 5️⃣ Run the System

```bash
python main.py
```

---

## 🎯 Usage

### Basic Usage

Simply run the main script and provide your project description when prompted:

```bash
python main.py
```

### Output Structure

Generated projects follow this structure:

```
workspace/
└── your-project-name/
    ├── main.py
    ├── utils.py
    ├── config.py
    ├── requirements.txt
    └── README.md
```

---

## 📁 Project Structure

```
langgraph_coding_pipeline/
│
├── main.py                 # Application entry point
├── graph.py               # LangGraph workflow definition
├── state.py               # Shared state management across agents
├── config.py              # Configuration and settings
│
├── agents/                # Agent implementations
│   ├── __init__.py
│   ├── manager.py         # Workflow orchestration agent
│   ├── architecture.py    # Project structure design agent
│   ├── code_writer.py     # Code generation agent
│   ├── documentation.py   # README generation agent
│   └── file_saver.py      # File system operations agent
│
├── workspace/             # Generated projects (auto-created)
│   └── [your-projects]/
│
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
└── README.md             # This file
```

---

## 🛠️ Requirements

### System Requirements

- **Python:** 3.8 or higher

### Python Dependencies

```txt
langchain>=0.1.0
langgraph>=0.0.20
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```env
# Required
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional
WORKSPACE_DIR=workspace
MODEL_NAME=gemini-pro
TEMPERATURE=0.7
```


## 📚 Documentation

### Agent Details

#### Manager Agent
Analyzes user input and determines the appropriate workflow mode:
- **Full Project Mode** – Complete project generation
- **Code Only Mode** – Generate code without architecture
- **Documentation Mode** – Create docs for existing code

#### Architecture Agent
Designs the project structure:
- File organization
- Module responsibilities
- Dependency relationships
- Best practice patterns

#### Code Writer Agent
Generates production-ready code:
- Clean, readable code
- Proper error handling
- Type hints and docstrings
- PEP 8 compliance

#### Documentation Agent
Creates comprehensive documentation:
- Project overview
- Installation instructions
- Usage examples
- API documentation

#### File Saver Agent
Manages file operations:
- Directory creation
- File writing
- Path management
- Conflict resolution

---

