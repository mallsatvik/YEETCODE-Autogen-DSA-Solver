YEETCODE – Agentic DSA Solver
YEETCODE is an AI-powered Data Structures & Algorithms problem solver built with:
Microsoft Autogen (multi-agent orchestration)
Ollama Mistral (local LLM backend)
Docker (safe sandbox for code execution)
Streamlit (interactive UI)

YEETCODE can:
Take a DSA problem statement as input.
Use an AI Problem Solver agent (powered by Mistral) to:
Plan a solution
Write Python code and test cases
Ask the Code Executor agent to run the code in Docker
Save the solution to a .py file
End the loop automatically once the task is complete.
Example Run
user : Write a Python code to reverse a linked list.
DSA_Problem_Solver_Agent :
Plan: I will implement a LinkedList class with a reverse method.
... (code + 3 test cases) ...
STOP


Result:
Code saved in linked_list_reverse.py
Tests executed inside Docker
Task completed

Tech Stack
Autogen (agent orchestration)
Ollama Mistral (local LLM model)
Docker (sandbox execution)
Streamlit (UI)
Python 3.10+

Project Structure
YEETCODE/
│── agents/
│   ├── problem_solver.py
│   ├── code_executor_agent.py
│
│── team/
│   └── dsa_team.py
│
│── config/
│   ├── settings.py
│   ├── constant.py
│   ├── docker_utils.py
│   └── docker_executor.py
│
│── main.py          # CLI entrypoint
│── app.py           # Streamlit UI
│── requirements.txt
│── .gitignore

Installation and Setup
1. Clone the repository
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
Create a .env file in the project root:
# Ollama local server (OpenAI-compatible endpoint)
OLLAMA_BASE_URL=http://localhost:11434/v1
5. Install Ollama and Mistral
Download Ollama: https://ollama.com/download
Pull the model and start the server:
ollama pull mistral
ollama serve
6. Run the solver
Run in CLI mode:
python main.py

Run with the Streamlit UI:
streamlit run app.py

Features
Multi-agent loop (Planner + Executor)
Automatic test case generation
Saves solutions to .py files
Sandboxed Docker execution
Streamlit user interface

Roadmap
Add Judge agent for test pass/fail reporting
Add support for C++ and Java execution
Add problem loaders (LeetCode, Codeforces)
Add metrics dashboard (success rate, iterations)
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

MIT License. See LICENSE for details.
