from openai import OpenAI
from apikey import apiKey
import os
from PIL import Image
import requests
from io import BytesIO
os.environ['OPENAI_API_KEY'] = apiKey
OpenAI.api_key = apiKey

client = OpenAI()



prompt = 'A cute puppy playing with a cute kitten' # for image
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