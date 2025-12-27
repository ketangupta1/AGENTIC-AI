# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv('GEMINI_API_KEY') ,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
Give answer only in python. And do not give any answer other tham coding, 
just say Sorry! I am designed to answer coding related questions.
"""


# Zero-shot Prompting: The model is given direct question or task without prior examples.

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you say a joke?"}
    ]
)

print(response.choices[0].message.content)