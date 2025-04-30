import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load('model.pkl')

st.title("💰 Healthcare Insurance Cost Predictor")

# Input fields
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Do you smoke?", ["No", "Yes"])
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])

# Preprocess inputs
input_dict = {
    'age': age,
    'sex': 0 if sex == 'Male' else 1,
    'bmi': bmi,
    'children': children,
    'smoker': 1 if smoker == 'Yes' else 0,
    'region_northwest': 1 if region == 'northwest' else 0,
    'region_southeast': 1 if region == 'southeast' else 0,
    'region_southwest': 1 if region == 'southwest' else 0
}

# Optional: BMI category
if bmi >= 30:
    input_dict['bmi_category_Obese'] = 1
else:
    input_dict['bmi_category_Obese'] = 0

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Predict
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
