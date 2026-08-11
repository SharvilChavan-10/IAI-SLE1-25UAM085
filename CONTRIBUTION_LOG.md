# AI Contribution Log

## Course

**02UAML204 - Introduction to Artificial Intelligence**

## Project

**Simple AI Chatbot**

## AI Tool Used

**GitHub Copilot Chat**

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

# Reflection

GitHub Copilot Chat was used as a coding assistant during the development of this project. It helped generate functions, conditions, loops, and chatbot responses based on my prompts.

I reviewed the AI-generated code before using it, modified parts when necessary, tested the program with different inputs, and verified that the features worked correctly.

This project helped me understand how AI-assisted programming can be used together with human review, testing, and debugging.