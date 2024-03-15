# 1. add the streamlit library to the project;

import streamlit as st

# 2. add the title to the app

st.title('My first streamlit app')

# 3. Running the app: streamlit run FILE_NAME.py

# 4. Header
st.header('This is the header')

# 5. SubHeader

st.subheader('This is SubHeader')

# 6. text

st.text('This is SubHeader')

# 7. Markdown

st.markdown('## this is markdown')


# 8. Button

st.button('This is Button')

# 8. Ckeckbox

st.checkbox('This is checkbox')

# 9. Radio

st.radio('Radio', ['one', 'two', 'three'])

# 9. SelectBox

st.selectbox('selectbox', ['one', 'two', 'three'])

# 9. file uploader

st.file_uploader('fileUploader', type=['png', 'jpeg', 'jpg'])

# 9. ColorPicker

st.color_picker('ColorPicker')

# 9. Date n time

st.date_input('Date')

st.time_input('time')

# 9. textInput

st.text_input('enter text', placeholder='enter your name')

# 9. numberInput

st.number_input('numberInput')

# 9. textArea

st.text_area('textarea')

# 9. sliders

st.slider('Slider', min_value=0,max_value=300, value=100)

# 9. progress bar

# import time
# my_bar = st.progress(0)
# for pcent in range(100):
#     time.sleep(0.1)
#     my_bar.progress(pcent+1)
#
# # 9. spinners
#
# with st.spinner('waiting...'):
#     time.sleep(2)

# 22. Adding columns
col1, col2, = st.columns(2)

with col1:
    st.header('Col1')
    st.subheader('This is Col1')

with col2:
    st.header('Col1')
    st.subheader('This is Col1')

# 23. Add image from file uploader and display it
image = st.file_uploader('Upload a image', type=['png', 'jpg'])
if image:
# python imaging library
    st.image(image, caption='Uploaded Image', use_column_width=True)