def chatbot():
    print("=" * 40)
    print("        SIMPLE CHATBOT")
    print("=" * 40)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
