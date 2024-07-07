import os
from openai import OpenAI
from dotenv import load_dotenv

# Variables
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
messages = []

# Work flow
print("------ Conversation Started ------\n")
print("****** Say bye to end the conversation *****\n")

user_input = input("What can I help you with?\n")

while user_input.lower() != "bye":  # Keep conversation going as long as user doesn't say bye
    messages.append({
        "role": "user",
        "content": user_input
    })

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens = 150
    )

    print(completion.choices[0].message.content)

    messages.append({
        "role": "system",
        "content": completion.choices[0].message.content
    })

    user_input = input()

print("\n------ Conversation Ended ------")
