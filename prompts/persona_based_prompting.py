# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI()

# You can give the chat of any person in example(100-150 chats) and you can see the LLM will give answer in the tone of that person.

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Ketan Kumar.
    You are acting on behalf of Ketan who is 25 years old Tech enthusiatic and 
    backend engineer. Your main tech stack is Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role":"user", "content": "who are you?" }
        ]
    )

print("Response:", response.choices[0].message.content)