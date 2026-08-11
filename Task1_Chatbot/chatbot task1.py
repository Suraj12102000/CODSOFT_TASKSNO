"""
CodSoft AI Internship - Task 1
Chatbot with Rule-Based Responses

"""

import random
import re
from datetime import datetime

BOT_NAME = "Codey"


# Topic-based responses 
TOPIC_RESPONSES = {
    "python": (
        "Python is a high-level, beginner-friendly programming language "
        "known for its simple, readable syntax and huge ecosystem of "
        "libraries."
    ),
    "ai": (
        "Artificial Intelligence (AI) is the simulation of human "
        "intelligence by machines, enabling them to learn, reason, and "
        "make decisions."
    ),
    "artificial intelligence": (
        "Artificial Intelligence (AI) is the simulation of human "
        "intelligence by machines, enabling them to learn, reason, and "
        "make decisions."
    ),
    "machine learning": (
        "Machine Learning is a subset of AI where systems learn patterns "
        "from data instead of being explicitly programmed. (Fun fact: "
        "this chatbot does NOT use Machine Learning — it's 100% rules!)"
    ),
    "chatbot": (
        "A chatbot is a program designed to simulate conversation with "
        "human users. I'm a rule-based chatbot, meaning I use keyword "
        "matching instead of AI models."
    ),
    "college": (
        "College is where you build your knowledge and skills for the "
        "future. Assignments like this one help you learn core "
        "programming concepts!"
    ),
    "exam": (
        "Exams can be stressful, but consistent study and good time "
        "management make a big difference. You've got this!"
    ),
    "assignment": (
        "Assignments help reinforce what you learn in class. This "
        "chatbot project is a great example of applying if-else logic "
        "and dictionaries in Python!"
    ),
    "project": (
        "This project is a Rule-Based Chatbot built using pure Python — "
        "no external AI services or Machine Learning involved."
    ),
    "weather": (
        "I don't have access to live weather data, but I hope it's "
        "sunny wherever you are! Try a weather app for real-time "
        "updates."
    ),
}

# ---------- Jokes ----------
JOKES = [
    "Why do programmers prefer dark mode?\nBecause light attracts bugs!",
    "Why do Python programmers wear glasses?\nBecause they can't C!",
    "Why did the computer go to therapy?\nIt had too many bytes of "
    "emotional baggage.",
    "How many programmers does it take to change a light bulb?\n"
    "None, that's a hardware problem.",
    "Why was the function sad after a breakup?\nIt just couldn't "
    "return anymore.",
]

# ---------- Motivational quotes ----------
QUOTES = [
    "\"The only way to do great work is to love what you do.\" - Steve Jobs",
    "\"Success is not final, failure is not fatal: it is the courage to "
    "continue that counts.\" - Winston Churchill",
    "\"Believe you can and you're halfway there.\" - Theodore Roosevelt",
    "\"Don't watch the clock; do what it does. Keep going.\" - Sam Levenson",
    "\"The future belongs to those who believe in the beauty of their "
    "dreams.\" - Eleanor Roosevelt",
]

QUOTE_KEYWORDS = ["motivation", "motivate", "quote", "inspire"]

# ---------- Unknown responses ----------
UNKNOWN_RESPONSES = [
    "I'm sorry, I didn't understand that.",
    "Can you ask in another way?",
    "Please ask something related to AI, Python, college, or general "
    "conversation.",
]


def get_greeting_response():
    responses = [
        "Hey there! How can I help you today?",
        "Hello! Nice to see you here.",
        "Hi! What's up?",
        "Hey! I'm here, ask me anything."
    ]
    return random.choice(responses)


def get_farewell_response():
    responses = [
        "Bye! Have a great day :)",
        "See you later!",
        "Goodbye, take care!",
        "It was nice talking to you, bye!"
    ]
    return random.choice(responses)


def get_thanks_response():
    responses = [
        "You're welcome!",
        "No problem at all!",
        "Anytime :)",
        "Glad I could help!"
    ]
    return random.choice(responses)


def check_topic_response(text):
    for keyword in sorted(TOPIC_RESPONSES, key=len, reverse=True):
        if keyword in text:
            return TOPIC_RESPONSES[keyword]
    return None


def respond(user_input):
    text = user_input.lower().strip()
    text = re.sub(r"[!?.]", "", text)

    # greetings 
    if re.search(r"\b(hi|hello|hey|hola|yo)\b", text):
        return get_greeting_response()

    # how are you 
    elif re.search(r"how are (you|u)", text):
        return "I'm just a program so I don't really have feelings, but thanks for asking! How about you?"

    # name 
    elif re.search(r"what('?s| is) your name", text) or "who are you" in text:
        return f"I'm {BOT_NAME}, a rule based chatbot made for the CodSoft AI internship task."

    elif re.search(r"my name is (\w+)", text):
        match = re.search(r"my name is (\w+)", text)
        name = match.group(1).capitalize()
        return f"Nice to meet you, {name}!"

    # time / date 
    elif "time" in text and "what" in text:
        now = datetime.now().strftime("%I:%M %p")
        return f"Right now it's {now} (according to my system clock)."

    elif "date" in text and "what" in text:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    # ---- capabilities ----
    elif re.search(r"what can you (do|help)", text):
        return "I can chat about basic stuff - greetings, my name, time, date, jokes, quotes, topics like AI/Python, and a bit of small talk."

    # ---- motivational quotes ----
    elif any(word in text for word in QUOTE_KEYWORDS):
        return random.choice(QUOTES)

    # ---- jokes ----
    elif "joke" in text:
        return random.choice(JOKES)

    # ---- thanks ----
    elif re.search(r"\b(thanks|thank you|thx)\b", text):
        return get_thanks_response()

    # ---- help ----
    elif text == "help":
        return "Try asking me things like: hi, what's your name, how are you, tell me a joke, give me a quote, what time is it, or ask about python/ai/college. Type bye to exit."

    # ---- farewell ----
    elif re.search(r"\b(bye|goodbye|exit|quit|see you)\b", text):
        return "__EXIT__"   

    # ---- topic based responses  ----
    else:
        topic_reply = check_topic_response(text)
        if topic_reply:
            return topic_reply

        return random.choice(UNKNOWN_RESPONSES)


def main():
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}, your friendly rule-based chatbot.")
    print(f"{BOT_NAME}: Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print(f"{BOT_NAME}: Say something na, don't leave me on read.")
            continue

        reply = respond(user_input)

        if reply == "__EXIT__":
            print(f"{BOT_NAME}: {get_farewell_response()}")
            break

        print(f"{BOT_NAME}: {reply}")


if __name__ == "__main__":
    main()
