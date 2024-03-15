from openai import OpenAI
from apikey import apiKey
import os
from PIL import Image
import requests
from io import BytesIO
os.environ['OPENAI_API_KEY'] = apiKey
OpenAI.api_key = apiKey

client = OpenAI()



# prompt = 'What is the capital of India' # for text
#
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": prompt}]
# )
#
# print('response')
# print(response)
#
# print(response.choices[0].message.content)
# print('Message Content:')


prompt = 'Capital of india' # for image
print('generating Image')

response = client.images.generate(
    model='dall-e-2',
    prompt= prompt,
    size='512x512',
    n=1,
)
print(response)

image_url = response.data[0].url
image = requests.get(image_url)
image = Image.open(BytesIO(image.content))
image.show()
# save image to a file
image.save('generated_image.png')