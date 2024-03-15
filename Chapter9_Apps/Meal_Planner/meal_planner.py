import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[2]))

from Chaper6_CodeBasics.online_module import *
from apikey import apiKey
import json

st.title("AI Meal Planner")

client = setup_openai(apiKey)

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ('Male', 'Female', 'Other'))
    weight = st.number_input('Weight (kg):', min_value=30, placeholder=80)

with col2:
    age = st.number_input('Age:', min_value=18, placeholder=22)
    height = st.number_input('Height (cm):', min_value=1, max_value=250, step=1, placeholder=170)

aim = st.selectbox('Aim', ('Lose', 'Gain', 'Maintain'))

user_data = f'''
                - I am a {gender}
                - My weight is {weight}kg
                - I am {age} years old
                - My height is {height}cm
                - My aim is to {aim} weight
            '''

output_format = '''
                    "range":"Range of ideal weight",
                    "target":"Target weight",
                    "difference":"Weight I need to loose or gain",
                    "bmi":"my BMI",
                    "meal_plan":"Meal plan for 7 days",
                    "total_days":"Total days to reach target weight",
                    "weight_per_week":"Weight to loose or gain per week",
                '''

prompt = user_data + ("given the information, generate a meal plan for me, follow the output format as follows, "
                      "give only JSON format nothing else and give the day as the JSON object and it should have 3 "
                      "keys and values, Breakfast, lunch, dinner"
                      "and this is the output format ") + output_format

if st.button('Generate Meal Plan'):
    progress_bar = st.progress(0)
    with st.spinner('Generating Meal Plan'):
        text_area_placeholder = st.empty()
        meal_plan = generate_text_openai_streamlit(client, prompt)
        meal_plan_json = json.loads(meal_plan)

        st.title("Meal Plan")
        col1, col2, col3 = st.columns(3)
        progress_bar.progress(25)
        with col1:
            st.subheader("Range")
            st.write(meal_plan_json["range"])
            st.subheader("Target")
            st.write(meal_plan_json["target"])

        with col2:
            st.subheader("BMI")
            st.write(meal_plan_json["bmi"])
            st.subheader("Days")
            st.write(meal_plan_json["total_days"])

        with col3:
            st.subheader(f"{aim}")
            st.write(meal_plan_json["difference"])
            st.subheader("Per week")
            st.write(meal_plan_json["weight_per_week"])
        progress_bar.progress(50)
        st.subheader("Meal plan for 7 days")

        table_data=[]

        for day, meals in meal_plan_json["meal_plan"].items():
            table_data.append({
                "Day": day,
                "Breakfast": meals.get("Breakfast", "-"),
                "Lunch": meals.get("Lunch", "-"),
                "Dinner": meals.get("Dinner", "-")
            })
        progress_bar.progress(100)
        df = pd.DataFrame(table_data)
        html_table = df.to_html(index=False, escape=False)
        st.write(html_table, unsafe_allow_html=True)
