def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. I can respond to 'hello', 'how are you', and 'bye'."
def run_chatbot():
    print("--- Basic Chatbot ---")
    print("Type 'bye' to exit the chat.\n")
    while True:
        user_msg = input("You: ")
        reply = chatbot_response(user_msg)
        print(f"Chatbot: {reply}")
        if user_msg.lower().strip() in ["bye", "goodbye", "exit"]:
            break
if __name__ == "__main__":
    run_chatbot()