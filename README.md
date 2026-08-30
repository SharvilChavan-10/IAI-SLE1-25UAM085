# AI Study Assistant - Basic Rule-Based Agent

This repository contains a basic rule-based conversational AI agent implemented in Python. The agent functions as an AI Study Assistant capable of handling standard conversational inputs and managing a simple, in-memory task list.

## Features
- **Conversational Queries:** Responds to standard inputs like `hello`, `how are you`, `thank you`, and `help`.
- **Task Management Agent Capabilities:**
  - `add task <task description>` - Adds a new task to the list.
  - `show tasks` - Displays all tasks with their current completion status (`[ ]` or `[✓]`).
  - `complete task <number>` - Marks a specific task number as completed.
- **Graceful Exit:** Safely exits the application when the user types `bye`.

---

## Prerequisites
To run this application, you only need to have Python installed on your system. No external libraries or third-party packages are required.
- **Python Version:** Python 3.x is recommended.

---

## How to Run the Code

Follow these quick steps to execute the program locally:

### Step 1: Open the Project Directory
Open your terminal, command prompt, or Visual Studio Code integrated terminal, and navigate to the directory where your project files are located.

### Step 2: Run the Script
Execute the main program script by running the following command:

```bash
python agent.py
```

### Step 3: Interacting with the Agent
Once the application starts, type any command into the prompt and press **Enter**. 

**Example Workflow:**
```text
Welcome to the Simple AI Chatbot! Type 'bye' to exit.
You: hello
Bot: Hello! How can I assist you today?

You: add task Study Python
Bot: Added task: Study Python

You: show tasks
Bot: Tasks:
1. [ ] Study Python

You: complete task 1
Bot: Task 1 completed: Study Python

You: show tasks
Bot: Tasks:
1. [✓] Study Python

You: bye
Bot: Goodbye! Have a great day!
```
