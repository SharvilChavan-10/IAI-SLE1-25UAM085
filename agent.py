# Simple AI Chatbot

# In-memory task list for simple task management.
tasks = []

def format_tasks():
    if not tasks:
        return "No tasks found."

    lines = []
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        lines.append(f"{index}. [{status}] {task['name']}")
    return "Tasks:\n" + "\n".join(lines)

def chatbot_response(user_input):
    # Basic responses based on user input
    text = user_input.strip()
    lower_text = text.lower()

    if lower_text.startswith("add task "):
        task_text = text[9:].strip()
        if not task_text:
            return "Please provide a task description after add task."
        tasks.append({"name": task_text, "done": False})
        return f"Added task: {task_text}"
    elif lower_text == "show tasks":
        return format_tasks()
    elif lower_text.startswith("complete task "):
        number_text = text[14:].strip()
        try:
            task_number = int(number_text)
        except ValueError:
            return "Invalid task number. Use the number shown in show tasks."

        if task_number < 1 or task_number > len(tasks):
            return "Task number out of range. Please check show tasks."

        tasks[task_number - 1]["done"] = True
        return f"Task {task_number} completed: {tasks[task_number - 1]['name']}"
    elif "hello" in lower_text:
        return "Hello! How can I assist you today?"
    elif "how are you" in lower_text:
        return "I'm just a bot, but I'm here to help you!"
    elif "thank you" in lower_text:
        return "You're welcome!"
    elif "help" in lower_text:
        return "Available commands: hello, how are you, thank you, help, bye, add task <task>, show tasks, complete task <number>."
    elif "bye" in lower_text:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"
    
def main():
    print("Welcome to the Simple AI Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()