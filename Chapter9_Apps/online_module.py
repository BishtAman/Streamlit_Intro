from openai import OpenAI
from apikey import apiKey
import os
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from pathlib import Path


############# setup the OpenAI API key ###############
def setup_openai(apiKey):
    os.environ['OPENAI_API_KEY'] = apiKey
    OpenAI.api_key = apiKey
    client = OpenAI()
    return client


################### OPEN AI AUDIO TO TEXT #####################
def generate_text_from_audio_openai(client, audio_file, model="whisper-1", language='en', response_format="text"):
    response = client.audio.transcriptions.create(
        model=model,
        file=audio_file,
        response_format=response_format
    )
    return response


###################### OPEN AI TEXT TO IMAGE ####################
def generate_image_openai(client, prompt, model='dall-e-2', size='512x512', n=1, ):
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        n=n,
    )
    image_url = response.data[0].url
    image = requests.get(image_url)
    image = Image.open(BytesIO(image.content))
    return image


###################### OPEN AI TEXT GENERATION ####################
def generate_text_openai_streamlit(client, prompt, text_area_placeholder=None, model="gpt-3.5-turbo",
                                   temperature=0.5, max_tokens=3000, top_p=1,
                                   frequency_penalty=0, presence_penalty=0,
                                   stream=True, html=False):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream,
    )
    complete_response = []
    for chunk in response:
        if chunk.choices[0].delta.content:
            complete_response.append(chunk.choices[0].delta.content)
            result_string = ''.join(complete_response)

            # AUTO SCROLL
            lines = result_string.count('\n') + 1
            avg_chars_per_line = 80
            lines += len(result_string) // avg_chars_per_line
            height_per_line = 20  # Adjust as needed
            total_height = lines * height_per_line

            if text_area_placeholder:
                if html:
                    text_area_placeholder.markdown(result_string, unsafe_allow_html=True)
                else:
                    text_area_placeholder.text_area("Generated Text", value=result_string, height=total_height)

    result_string = ''.join(complete_response)
    words = len(result_string.split())
    st.text(f"Total Words Generated: {words}")

    return result_string


###################### OPEN AI TEXT TO AUDIO ####################
def generate_audio_form_text(client, prompt, voice_type, model="tts-1"):
    response = client.audio.speech.create(
        model=model,
        voice=voice_type,
        input=prompt
    )
    speech_file_path = Path("speech.mp3")
    response.stream_to_file(speech_file_path)
    return speech_file_path


def main():
    client = setup_openai(apiKey)

    ############# AUDIO GENERATION ############
    st.title("Text to Speech Converter")
    prompt = st.text_area("Enter the text you want to convert to speech:", height=150)
    voice_type = st.selectbox(
        "Choose the voice:",
        ["alloy", "echo", "fable", "onyx", "nova", "shimmer"])
    # Convert button
    if st.button("Convert to Speech"):
        with st.spinner("Generating Audio..."):
            speech_file_path = generate_audio_form_text(client, prompt, voice_type)
            if speech_file_path:
                # Display audio player and download link

                audio_file = open(speech_file_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                st.download_button(label="Download Speech",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")

    ############# TEXT GENERATION ############
    st.title("Text Generation using OpenAI API")
    prompt = st.text_input("Enter your prompt", value="Write a short note on India")
    text_area_placeholder = st.empty()
    if st.button("Generate Text"):
        result = generate_text_openai_streamlit(client, prompt, text_area_placeholder, html=True)

    ############# IMAGE GENERATION ############
    st.title("Logo Generation using OpenAI API")
    logo_type = st.selectbox(
        "Choose the voice:",
        ["cartoon", "realistic", "simple", "unique"])
    logo_theme = st.text_input("Enter your prompt", value="")
    prompt = f'Create a logo on {logo_theme}, that should be {logo_type}'
    if st.button("Generate Image"):
        with st.spinner("Generating Image..."):
            image = generate_image_openai(client, prompt)
            st.image(image)

    ############# AUDIO TRANSCRIPTION ############
    st.title("Audio Transcription using OpenAI API")
    audio_file = st.file_uploader('Choose an audio file...', type=['mp3', 'wav'])
    if audio_file:
        if st.button("Transcribe"):
            st.audio(audio_file, format="audio/wav")
            with st.spinner("Transcribing audio..."):
                result = generate_text_from_audio_openai(client, audio_file)
                st.write(result)


if __name__ == '__main__':
    main()
