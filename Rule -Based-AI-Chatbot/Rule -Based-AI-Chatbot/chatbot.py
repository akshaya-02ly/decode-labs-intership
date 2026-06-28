#project 1-Rule Based AI Chatbot project
print("=" * 40)
print("      WELCOME TO AI CHATBOT")
print("=" * 40)
print("Type 'exit' to end the chat.\n")

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "who created you": "I was created using Python.",
    "what can you do": "I can answer simple predefined questions.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!"
}

while True:
    user = input("You: ").strip().lower()

    if user == "exit" or user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    elif user in responses:
        print("Bot:", responses[user])
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")