import torch
from transformers import pipeline
import streamlit as st

################### LOCAL AUDIO TO TEXT (Whisper) #####################

model_path = "Models/models--openai--whisper-medium/snapshots/abdf7c39ab9d0397620ccaea8974cc764cd0953e"


def load_model_audio(model_path, chunk_length_s=30, device="cpu"):
    model = pipeline("automatic-speech-recognition", model=model_path, chunk_length_s=chunk_length_s, device=device)

    return model


def save_uploaded_audio_file(uploaded_file):
    pass


def generate_text_from_audio_whisper(model, audio_file):
    output = model("../../Resources/audio.mp3")["text"]

    print(output)


def main():
    ############# AUDIO TRANSCRIPTION ############
    st.title("Audio Transcription using Local Whishper")
    audio_file = st.file_uploader('Choose an audio file...', type=['mp3', 'wav'])

    if audio_file:
        if st.button("Transcribe"):
            st.audio(audio_file, format="audio/wav")
            with st.spinner("Transcribing audio..."):
                result = generate_text_from_audio_whisper(client, audio_file)
                st.write(result)


if __name__ == '__main__':
    main()
