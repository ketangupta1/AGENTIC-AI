from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

response = openai_client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Whats in the image? Describe"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://images.pexels.com/photos/35542452/pexels-photo-35542452.jpeg?_gl=1*1npc9vh*_ga*MTM3MzkwNDIxOS4xNzY4NjQ4Mjkz*_ga_8JE65Q40S6*czE3Njg2NDgyOTMkbzEkZzEkdDE3Njg2NDgzMjkkajI0JGwwJGgw"}
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
