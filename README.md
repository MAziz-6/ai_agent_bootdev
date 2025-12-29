# 🤖 MyMiniAgent: A Toy AI Coding Assistant

`MyMiniAgent` is a lightweight, experimental AI agent powered by the **Google Gemini API**. It demonstrates how an LLM can use tool calling to interact with a local file system—listing files, reading code, running Python scripts, and applying fixes autonomously.

This project was built as part of the [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python) course by **Boot.dev**.

> [!CAUTION]
> ### ⚠️ Security Warning & Disclaimer
> This is a **toy project** and is **not secure** for production use.
> * **Code Execution:** The agent can execute Python scripts and overwrite files directly on your host machine.
> * **No Sandboxing:** Unlike professional tools (like Cursor or Claude Code), this agent does not run in a container. It has the same permissions as your terminal user.
> * **Risk of Data Loss:** Malicious prompts or LLM hallucinations could result in the unintended deletion or modification of your files.
> * **Usage:** Only run this in a dedicated, isolated test directory. **Use at your own risk.**

---

## ✨ Features

* **Agentic Loop:** Uses a feedback loop to iterate on complex tasks until they are solved.
* **Tool Calling:** The agent can choose to `list_files`, `read_file`, `write_file`, or `execute_python` based on its own logic.
* **Autonomous Debugging:** Capable of finding and fixing logic errors (e.g., correcting mathematical operator precedence).
* **Gemini-Powered:** Utilizes `gemini-2.0-flash` for fast and intelligent reasoning.

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.10+
* [uv](https://github.com/astral-sh/uv) (Recommended package manager)
* A Google AI Studio API Key.

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/yourusername/myminiapp.git](https://github.com/yourusername/myminiapp.git)
cd myminiapp

# Install dependencies
uv add google-genai python-dotenv
```

### 3. Configuration
Create a new `.env` file in the root directory:
```bash
GEMINI_API_KEY='your_api_key_here'
```

### 4. usage
Run the agent with a specif task:
```bash
python main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```
The example above relates to the example from boot.dev where we intentionlly altered the precedence of the addition (+) operation in the calculator to 3. 

## 🛠 Project Structure

The project is organized into modular components to separate the agent's logic, its tools, and its instructions.

### Directory Layout
```text
├── main.py          # The core agentic loop and API orchestration
├── tools.py         # Definitions for file I/O and code execution
├── prompts.py       # System instructions and persona definitions
├── .env             # API keys and environment variables (gitignored)
└── README.md        # Project documentation
```
## 🎓 Credits & Acknowledgments

This project was developed as part of the [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python) course on **Boot.dev**. 

A huge thank you to **Lane Wagner** and the entire **Boot.dev** team for providing the foundational curriculum, tool-calling patterns, and the "Agentic Loop" concepts used to build this assistant.

---

## 📜 License & Use

This project is intended strictly for **personal educational purposes** as part of the Boot.dev curriculum. 

While the code is available for review, it is not intended for production use or redistribution as a standalone product. If you are also a student of Boot.dev, please ensure you follow their [Academic Integrity](https://www.boot.dev/community/academic-integrity) guidelines when referencing this repository.
