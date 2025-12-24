# Few Shot Prompting
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
Examples:
Q: Can you explain a+b whole square?
A: Sorry Sorry! I am designed to answer coding related questions.

Q: Can you write code to add two numbers?
A: def(a, b):
        return a+b
"""


# Few-shot Prompting: The model is given direct question or task with few prior examples. This examples increses the accuracy of the answer.
# In reality few-shots prompting are widely used.

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you say a+b whole square?"}
    ]
)

print(response.choices[0].message.content)