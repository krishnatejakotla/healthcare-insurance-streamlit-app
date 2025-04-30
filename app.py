import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('model.pkl')

st.title("💰 Healthcare Insurance Cost Predictor")

# Input fields
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])

# Preprocess input
input_dict = {
    'age': age,
    'sex': 0 if sex == 'Male' else 1,
    'bmi': bmi,
    'children': children,
    'smoker': 1 if smoker == 'Yes' else 0,
    'region_northwest': 0,
    'region_southeast': 0,
    'region_southwest': 0,
    'region_northeast': 0  # ← previously missing!
}

# Set selected region to 1
input_dict[f"region_{region}"] = 1

# BMI category (custom feature)
input_dict['bmi_category_Obese'] = 1 if bmi >= 30 else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Reorder and typecast columns
required_cols = ['age', 'sex', 'bmi', 'children', 'smoker',
                 'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest',
                 'bmi_category_Obese']

for col in required_cols:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[required_cols]
input_df = input_df.astype({
    'age': 'int',
    'sex': 'int',
    'bmi': 'float',
    'children': 'int',
    'smoker': 'int',
    'region_northeast': 'int',
    'region_northwest': 'int',
    'region_southeast': 'int',
    'region_southwest': 'int',
    'bmi_category_Obese': 'int'
})

# Predict and display result
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
