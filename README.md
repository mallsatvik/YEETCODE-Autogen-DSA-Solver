📘 YEETCODE – Agentic DSA Solver

YEETCODE is an AI-powered Data Structures & Algorithms problem solver built with:

🤖 Microsoft Autogen (multi-agent orchestration)

🦙 Ollama Mistral (local LLM backend)

🐳 Docker (safe sandbox for code execution)

🖥️ Streamlit (interactive UI)

YEETCODE can:

Take a DSA problem statement (input by user).

Use an AI Problem Solver agent (Mistral) to:

Plan a solution

Write Python code + test cases

Ask the Code Executor agent to run the code in Docker

Save the solution to a .py file

Stop automatically once the task is done.

🚀 Demo (example run)
user : Write a Python code to reverse a linked list.
DSA_Problem_Solver_Agent :
Plan: I will implement a LinkedList class with a reverse method.
... (code + 3 test cases) ...
STOP


✅ Code is saved in linked_list_reverse.py
✅ Tests executed inside Docker
✅ Task marked complete

🛠 Tech Stack

LLM Orchestration: Autogen

LLM Backend: Ollama Mistral
 (local, no API costs)

Execution Sandbox: Docker (isolated code runs)

Frontend: Streamlit

📂 Project Structure
YEETCODE/
│── agents/
│   ├── problem_solver.py      # DSA solver agent
│   ├── code_executor_agent.py # Executes code in Docker
│
│── team/
│   └── dsa_team.py            # Round-robin group chat config
│
│── config/
│   ├── settings.py            # Model client (Ollama / Autogen)
│   ├── constant.py            # Config: MODEL, STOP token, etc.
│   ├── docker_utils.py        # Start/stop Docker helpers
│   └── docker_executor.py     # Docker code executor
│
│── main.py                    # CLI entrypoint
│── app.py                     # Streamlit UI
│── requirements.txt
│── .gitignore

⚡ Installation & Setup
1. Clone the repo
git clone https://github.com/mallsatvik/YEETCODE-Agentic-DSA-Solver.git
cd YEETCODE-Agentic-DSA-Solver

2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate      # Windows
# or
source .venv/bin/activate     # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Setup .env

Create a .env file in project root:

# Ollama local server (OpenAI-compatible endpoint)
OLLAMA_BASE_URL=http://localhost:11434/v1

5. Install Ollama + Mistral

Download Ollama

Run:

ollama pull mistral
ollama serve

6. Run the solver

CLI mode:

python main.py


Web UI (Streamlit):

streamlit run app.py

🎯 Features

🔄 Multi-agent loop (Planner + Executor)

✅ Automatic test cases generation

💾 Saves code to .py files

🛡️ Sandboxed Docker execution

🖼️ Clean Streamlit interface

📌 Roadmap

 Add Judge agent for ✅ / ❌ test reporting

 Add support for C++ / Java execution

 Add problem loaders (LeetCode, Codeforces)

 Add metrics dashboard (success rate, iterations)

🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

📜 License

MIT License. See LICENSE for details.

✨ Built with love by @mallsatvik
