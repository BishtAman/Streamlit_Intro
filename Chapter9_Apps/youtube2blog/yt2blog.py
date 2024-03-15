from youtube_transcript_api import YouTubeTranscriptApi
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from Chaper6_CodeBasics.online_module import *
from Chaper6_CodeBasics.apikey import *

st.title("YouTube to Blog")

client = setup_openai(apiKey)


def get_youtube_video_id(url):
    if 'youtube.com' in url or 'youtu.be' in url:
        # Extract video ID using different patterns for different types of URLs
        if 'youtube.com' in url:
            video_id = url.split('v=')[1]
            ampersand_pos = video_id.find('&')
            if ampersand_pos != -1:
                video_id = video_id[:ampersand_pos]
        else:
            video_id = url.split('/')[-1]

        return video_id
    else:
        return "Invalid YouTube URL"


def get_transcript(url):
    video_id = get_youtube_video_id(url)
    img_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join(entry['text'] for entry in transcript_list)

    return [transcript_list, transcript_text, img_url]


output_format = ("""
                    <h1> Blog Title </h1>
                    <h1> Table of Contents </h1><li> Links of content </li>
                    <h1> Introduction </h1><p> introduction </p>
                    <h1> Heading of section </h1><p> content </p>
                    .
                    .
                    .
                    .
                    <h1> Heading of section </h1><p> content </p>
                    <h4> Code if its a coding video </h4>
                    <h1> FAQ </h1><p> Question answers </p>
                    <h1> Conclusion </h1><p> conclusion </p>
                """)

url = st.text_input("Enter the video url", placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if st.button("Create Blog"):

    transcript_list, transcript_text, img_url = get_transcript(url)
    st.image(img_url, caption="Video Thumbnail")

    with st.spinner("Generating Blog Post..."):

        st.write("Transcript received - Word Count: " + str(len(transcript_text.split())))

    with st.spinner("Generating Summary"):

        prompt = f" You are a youtuber and you wan to write a blog post about your video. Using the below transcript " \
                 f" of the video create a long and detailed summary with a title, headings and conclusion  " \
                 f" that will be later used to generate the blog"  \
                 f" ${transcript_text}"

        text_area_placeholder = st.empty()

        summary = generate_text_openai_streamlit(client, prompt, text_area_placeholder)
        text_area_placeholder.empty()

    with st.spinner('Generating Blog...'):


        # st.write(summary)
        blog_prompt = f" Create a blog post from the following summary: {summary} " \
                 f" using the following format: {output_format} " \

        text_area_placeholder = st.markdown("", unsafe_allow_html=True)

        blog = generate_text_openai_streamlit(client, blog_prompt, text_area_placeholder, html=True)

        # st.write("Blog Generated - Word Count: " + str(len(blog.split())))
        st.video(url)