# AI Contribution Log - SLE -1
- PRN:-25UAM085
- Name:-Chavan Sharvil Sudhakar 
- Date:- 10-08-2026
## Course

**02UAML204 - Introduction to Artificial Intelligence**

## Project

**Simple AI Chatbot**

## AI Tool Used

**GitHub Copilot Chat**

**ChatGPT**

---

# Step 1 - Created Chatbot Response Function

### Prompt Given to GitHub Copilot

Create a Python function named `chatbot_response(user_input)` that responds to:

- hello
- how are you
- bye

Use only standard Python.

### AI Contribution

- Generated the `chatbot_response()` function.
- Suggested the `if-elif-else` conditions.
- Generated the initial chatbot responses.

### My Contribution

- Reviewed the generated code.
- Tested the function with different inputs.
- Verified that each response works correctly.

---

# Step 2 - Created Main Chatbot Loop

### Prompt Given to GitHub Copilot

Generate the main program that repeatedly asks the user for input, calls `chatbot_response()`, prints the response, and exits when the user types "bye". Use only standard Python.

### AI Contribution

- Generated the `main()` function.
- Generated the `while True` loop.
- Added user input and output statements.
- Added the exit condition for `"bye"`.

### My Contribution

- Reviewed the generated code.
- Added the following code to execute the `main()` function:

```python
if __name__ == "__main__":
    main()
```

- Tested the chatbot.
- Verified that the chatbot exits correctly when the user types `"bye"`.

---

# Step 3 - Added Thank You Response

### Prompt Given to GitHub Copilot

Add a response for when the user says "thank you" to the existing chatbot. Do not modify the other responses.

### AI Contribution

- Suggested the `elif` condition for `"thank you"`.
- Generated the response `"You're welcome!"`.

### My Contribution

- Reviewed the generated suggestion.
- Added the feature to the chatbot.
- Tested the `"thank you"` input.
- Verified that existing chatbot responses still work.

---

# Step 4 - Added Help Command

### Prompt Given to GitHub Copilot

I have a beginner Python rule-based chatbot with a
`chatbot_response(user_input)` function.

Add a help command.

Requirements:

- When the user types `"help"`, display the available commands.
- Commands should include hello, how are you, thank you, help, and bye.
- Use only standard Python.
- Do not rewrite unrelated parts of my code.
- Explain what you changed.

### AI Contribution

- Suggested the `help` condition.
- Generated the list of available commands.
- Generated the help response.

### My Contribution

- Reviewed the generated code.
- Accepted the relevant suggestion.
- Tested the help command.
- Verified that the existing commands still work.

---
---

# Step 5 - Added Task Manager Agent Capability

### Prompt Given to GitHub Copilot

I have a beginner-friendly Python rule-based chatbot.

I want to add a simple task manager capability to make it more agent-like.

Requirements:

- `"add task <task>"` should add a task to an in-memory Python list.
- `"show tasks"` should display all tasks.
- `"complete task <number>"` should mark a task as completed.
- Store task information using a simple Python data structure.
- Handle invalid task numbers without crashing.
- Use only Python standard features.
- Do not use `eval()`.
- Do not remove my existing chatbot features.
- Keep the code beginner-friendly.
- Explain exactly what code was added and where it should be placed.

### AI Contribution

- Suggested an in-memory task list for storing tasks.
- Generated the task addition logic.
- Generated the task display logic.
- Generated the task completion logic.
- Added validation for invalid task numbers.
- Suggested changing the task conditions to an `if-elif` chain so that the final fallback response does not execute before the task commands.

### My Contribution

- Reviewed the Copilot-generated code.
- Checked the task-management logic.
- Tested adding a task.
- Tested displaying tasks.
- Tested completing a task.
- Tested invalid task numbers.
- Verified that the existing chatbot features continue to work.
- Accepted and modified the Copilot suggestion where necessary.

### Testing

Example commands tested:

```text
You: add task Study Python
Bot: Added task: Study Python

You: show tasks
Bot: 1. Study Python

You: complete task 1
Bot: Task 1 completed: Study Python
```

### Result

The chatbot was extended with a basic task-management capability. It can receive a task-related command, identify the requested action, modify its internal task list, and provide a response to the user.

This makes the project a basic rule-based conversational agent rather than only a fixed-response chatbot.
# Reflection

GitHub Copilot Chat was used as a coding assistant during the development of this project. It helped generate functions, conditions, loops, and chatbot responses based on my prompts.

I reviewed the AI-generated code before using it, modified parts when necessary, tested the program with different inputs, and verified that the features worked correctly.

This project helped me understand how AI-assisted programming can be used together with human review, testing, and debugging.
