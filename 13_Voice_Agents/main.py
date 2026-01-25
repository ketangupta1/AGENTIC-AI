from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
import asyncio

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

openai_client = OpenAI()
openai_async_client = AsyncOpenAI()

async def tts(text:str):
    async with openai_async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=text,
        instructions="Speak in a cheerful and positive tone.",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

def main():
    r = sr.Recognizer() # Speech to Text recognizer

    SYSTEM_PROMPT = """
                You are an expert voice agent. You are given the transcript of what user said in the voice.
                You need to output that as an voice agent, as whatever you will be giving output will be 
                translated back to voice to the user.
            """
    
    messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        with sr.Microphone() as source: # Mic Access
            r.adjust_for_ambient_noise(source)  # Noise cancellation, cutting background noise
            r.pause_threshold = 2   # Stop listening if the speaker is silent for 2 seconds

            print("Speak Something...")
            audio = r.listen(source)

            print("Processing Audio...(STT)")
            stt = r.recognize_google(audio)

            print("You said: ",stt )

            messages.append({"role": "user", "content": stt})            

            response = openai_client.chat.completions.create(
                model = "gpt-4.1-mini",
                messages = messages
            )

            print("AI response: ", response.choices[0].message.content)
            asyncio.run(tts(response.choices[0].message.content))

main()