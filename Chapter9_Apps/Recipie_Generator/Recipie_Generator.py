import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from Chaper6_CodeBasics.online_module import *
from Chaper6_CodeBasics.apikey import *
st.title("AI Recipe Generator")

client = setup_openai(apiKey)

output_format = ("""
                    <h1> Fun title of recipe </h1>
                    <h1> Table of Contents </h1><li> Links of content </li>
                    <h1> Introduction </h1><p> dish introduction </p>
                    <h1> Country of Origin </h1><p> Country of Origin </p>
                    <h1> Ingredients </h1><li> Ingredients list </li>
                    <h1> Cooking </h1><li> Cooking steps list </li>
                    <h1> FAQ </h1><p> Question answers </p>
                """)

recipe = st.text_input("Enter your prompt...", placeholder="Chicken Biryani")
image_prompt = recipe + "realistic" + "cinematic"
if st.button("CreateRecipe"):
    with st.spinner("Generating Recipie..."):
        image = generate_image_openai(client, image_prompt)
        st.image(image, caption=recipe, use_column_width=True)

    with st.spinner("Generating Recipie..."):
        text_area_placeholder = st.markdown("", unsafe_allow_html=True)

        prompt = f" Create a long and detailed cooking recipe for the dish named {recipe}. " \
                 f" Include preparation steps and cooking tips. "  \
                 f" Follow the following format  {output_format} "

        generate_text_openai_streamlit(client, prompt, text_area_placeholder, html=True)