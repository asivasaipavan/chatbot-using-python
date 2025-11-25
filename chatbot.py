import datetime

print("🤖 Chatbot: Hello! I am your friendly rule-based chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have an amazing day 🌟")
        break

    elif user in ["hi", "hello", "hey", "hii", "hola"]:
        print("Chatbot: Hello! How can I help you today? 😊")

    elif "your name" in user:
        print("Chatbot: I am ChatBot 2.0 — built using simple Python rules!")

    elif "who created you" in user or "developer" in user:
        print("Chatbot: I was created by AMBERKAR SIVA SAI PAVAN in Python.")

    elif "how are you" in user:
        print("Chatbot: I'm doing great! Thanks for asking. What about you?")

    elif "i am fine" in user or "i'm fine" in user:
        print("Chatbot: Happy to hear that! 😄")

    elif "time" in user:
        print("Chatbot:", datetime.datetime.now().strftime("Current time is %I:%M %p"))

    elif "date" in user:
        print("Chatbot:", datetime.datetime.now().strftime("Today's date is %d-%m-%Y"))

    elif "weather" in user:
        print("Chatbot: I can't check live weather, but I hope it's pleasant where you are 🌤️")

    elif "study" in user or "studies" in user:
        print("Chatbot: Study consistently, practice DSA daily, and revise your notes!")

    elif "motivate" in user or "motivation" in user:
        print("Chatbot: Believe in yourself! Every expert was once a beginner 💪🔥")

    elif "python" in user:
        print("Chatbot: Python is great for data science, AI, automation, and backend development.")

    elif "c++" in user or "cpp" in user:
        print("Chatbot: C++ is powerful for system-level programming and CP.")

    elif "programming" in user:
        print("Chatbot: Programming improves problem-solving. Keep coding every day!")

    elif "college" in user or "cmr" in user:
        print("Chatbot: CMR Engineering College is a great place to learn Data Science!")

    elif "joke" in user:
        print("Chatbot: Why did the computer catch a cold? Because it forgot to close its Windows! 🤣")

    elif "life" in user:
        print("Chatbot: Life is a journey. Stay calm, work hard, and trust the process 🌱")

    else:
        print("Chatbot: Sorry, I didn’t understand that. Try asking something else! 😊")
