# AI Contribution Log - SLE -1
- PRN:-25UAM085
- Name:-Chavan Sharvil Sudhakar
- Division:-B
- Date:- 10-08-2026

## Course

**02AML204 - Introduction to Artificial Intelligence**
  
## 1. AI Tools Used
* **GitHub Copilot Chat** – Used throughout development as the primary coding assistant for step-by-step function generation and feature extension.

## 2. AI-Generated Code
* **Function `chatbot_response()`** – Generated the base structure and the initial `if-elif-else` conditional branches for basic greetings (`hello`, `how are you`, `bye`, `thank you`, `help`).
* **Function `main()`** – Generated the core program runtime loop, user input handling, and the terminal exit condition.
* **Task Manager Logic** – Generated the in-memory task list structure along with the parsing logic for `add task`, `show tasks`, and `complete task`.
* **Architecture Restructuring** – Suggested consolidating independent conditional blocks into a unified `if-elif` chain to prevent premature fallback responses.

## 3. My Own Contribution
* **Architecture Execution Block** – Implemented the `if __name__ == "__main__": main()` structure to properly handle standalone script execution.
* **Prompt Engineering & Constraints** – Iteratively designed scoped prompts enforcing security limitations (e.g., explicitly forbidding `eval()`), forcing code modularity, and keeping logic beginner-friendly.
* **Selective Integration & Testing** – Manually reviewed every code snippet suggested by Copilot and systematically tested edge cases for all interactive commands.

## 4. Issues Found in AI Code & Fixes
* **Logic Ordering Bug** – The AI placed the fallback response block ahead of the task manager parsing, causing valid task commands to trigger an error message. I restructured this into a single coherent `if-elif` chain.
* **Security Flaw Mitigated Proactively** – The AI's initial approach to parsing numbers leaned toward generic evaluation. I explicitly restricted it from using unsafe functions like `eval()`, directing it to use clean type-casting via `int()` protected by a `try-except ValueError` guard.
* **Missing Bounds Validation** – The AI's task completion module failed to verify index limits, leading to potential crashes from out-of-range inputs. I added explicit boundary validation constraints (`task_number < 1 or > len(tasks)`) to gracefully handle invalid numbers.
