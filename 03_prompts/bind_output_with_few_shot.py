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
Strictly follow the output in Json format.
Output format: 
{{
    "code": "string" or null,
    "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain a+b whole square?
A: {{"code": null, isCodingQuestion: False}}

Q: Can you write code to add two numbers?
A: {{"code": "def(a, b):
        return a+b", isCodingQuestion: True}}
"""


# In this way we can bind the LLM output and we can extract output from the response easily. Like we can direcly add .code for getting the code

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you say a+b whole square?"}
    ]
)

print(response.choices[0].message.content)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you write code for square of two num?"}
    ]
)

print(response.choices[0].message.content)