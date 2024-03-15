import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from Chaper6_CodeBasics.online_module import *
from Chaper6_CodeBasics.apikey import *

st.title("Free Logo Generator")

client = setup_openai(apiKey)

logo_theme = st.text_input("Enter your prompt...", placeholder="A coffee shop")
# logo_type = st.selectbox(
#     "Choose the voice:",
#     ["cartoon", "realistic", "simple", "unique"])

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    check1 = st.checkbox("Colorful")
with col2:
    check2 = st.checkbox("B&W")
with col3:
    check3 = st.checkbox("Minimalistic")
with col4:
    check4 = st.checkbox("Detailed")
with col5:
    check5 = st.checkbox("Circle")

image_prompt = "create a logo of " + logo_theme + "logo that should beflo "

if check1:
    image_prompt += " Colorful"
if check2:
    image_prompt += " B&W"
if check3:
    image_prompt += " Minimalistic"
if check4:
    image_prompt += " Detailed"
if check5:
    image_prompt += " Circle"

try:
    if st.button("Create Logo"):
        with st.spinner("Generating Logo..."):
            image = generate_image_openai(client, image_prompt)
            st.image(image, caption=logo_theme, use_column_width=True)
except Exception as e:
    # # Handle any exceptions that occur during logo generation
    # error_message = str(e)
    # if hasattr(e, 'response') and e.response is not None:
    #     error_message = e.response.json().get('error', {}).get('message', error_message)
    st.error(f"Error occurred: We're sorry, but the provided prompt contains inappropriate content and cannot be "
             f"processed.")
