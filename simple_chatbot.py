import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Variables
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
messages = []

# Work flow
def communicate(user):
    messages.append({
        "role": "user",
        "content": user
    })

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens = 150
    )

    messages.append({
        "role": "system",
        "content": completion.choices[0].message.content
    })

    return completion.choices[0].message.content

# Create interface
demo = gr.Interface(
    fn=communicate,
    inputs=["text"],
    outputs=["text"],
    title = "ChatGPT Assistant"
)

demo.launch()