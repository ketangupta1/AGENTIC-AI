from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Hey There!"
)

print(response.output_text)


# We can use google gemini with openAI compatible