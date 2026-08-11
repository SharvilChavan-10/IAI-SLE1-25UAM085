# Simple AI Chatbot

def chatbot_response(user_input):
    # Basic responses based on user input
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but I'm here to help you!"
    elif "thank you" in user_input.lower():
        return "You're welcome!"
    elif "help" in user_input.lower():
        return "Available commands: hello, how are you, thank you, help, bye."
    elif "bye" in user_input.lower():
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