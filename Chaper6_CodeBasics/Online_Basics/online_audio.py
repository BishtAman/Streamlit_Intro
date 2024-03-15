from openai import OpenAI
from apikey import apiKey
import os

os.environ['OPENAI_API_KEY'] = apiKey
OpenAI.api_key = apiKey

client = OpenAI()

audio_file = open("../../resources/audio.mp3", "rb")

print("Transcribing audio...")

response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(response)

