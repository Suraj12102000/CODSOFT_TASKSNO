# Task 1 - Chatbot with Rule-Based Responses

This is Task 1 of my CodSoft Artificial Intelligence Internship.

## About
A simple chatbot built in Python that responds to user messages using
if-else conditions and regex pattern matching (rule-based approach, no
ML/NLP libraries used). The goal of this task was to understand basic
conversation flow and how simple NLP-style bots work under the hood.

## Features
- Responds to greetings (hi, hello, hey...)
- Tells you its name and remembers yours if you introduce yourself
- Tells the current time and date
- Can crack a joke (5 different ones, picked randomly)
- Shares a motivational quote if you ask for "motivation"/"quote"/"inspire"
- Explains topics like Python, AI, Machine Learning, chatbots, college, exams, assignments, projects, and weather using a keyword dictionary
- Handles thank you / goodbye messages
- Has a fallback response for anything it doesn't understand

## How it works
User input is converted to lowercase and cleaned up a bit, then matched
against a set of regex patterns in an if/elif chain inside the `respond()`
function. Based on which pattern matches, it picks a reply (sometimes
randomly from a list of a few options so it doesn't sound too repetitive).

For general knowledge topics (Python, AI, ML, chatbot, college, exam,
assignment, project, weather), the input is instead checked against a
`TOPIC_RESPONSES` dictionary of keyword -> explanation pairs. If nothing
matches at all, a random reply from `UNKNOWN_RESPONSES` is used as the
fallback.

## How to run
```
python chatbot.py
```
Then just start typing in the terminal. Type `bye` to exit.

## Tech used
- Python 3
- `re` module for pattern matching
- `random` for varying responses
- `datetime` for time/date replies

## Sample conversation
```
Codey: Hi! I'm Codey, your friendly rule-based chatbot.
Codey: Type 'help' to see what I can do, or 'bye' to exit.

You: hi
Codey: Hey! I'm here, ask me anything.
You: what's your name
Codey: I'm Codey, a rule based chatbot made for the CodSoft AI internship task.
You: tell me a joke
Codey: Why did the computer go to therapy? It had too many unresolved issues.
You: bye
Codey: Bye! Have a great day :)
```

## Internship
This project is part of the CodSoft AI Internship program.
#codsoft #internship #artificialintelligence
