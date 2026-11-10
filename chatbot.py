def get_response(message):
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi! How can I help you?"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks! How are you?"
    elif message in ("what is your name", "what is your name?"):
        return "I'm a simple Python chatbot."
    elif message in ("help",):
        return "You can say hello, ask how I am, or type bye to exit."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can answer."


def run_chatbot():
    print("=== BASIC CHATBOT ===")
    print("Chat with me! Type 'help' for options or 'bye' to exit.")

    while True:
        user_message = input("You: ")
        response = get_response(user_message)
        print("Bot:", response)

        if user_message.strip().lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    run_chatbot()
