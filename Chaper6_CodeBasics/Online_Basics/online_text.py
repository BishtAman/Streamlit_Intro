from openai import OpenAI
from apikey import apiKey
import os

os.environ['OPENAI_API_KEY'] = apiKey
OpenAI.api_key = apiKey

client = OpenAI()



prompt = 'What is the capital of India' # for text

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print('response')
print(response)

print(response.choices[0].message.content)
print('Message Content:')

