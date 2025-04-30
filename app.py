import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and its expected feature names
model = joblib.load('model.pkl')
expected_cols = model.feature_names_in_  # This will avoid mismatch errors

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
    'region_northeast': 0,
    'region_northwest': 0,
    'region_southeast': 0,
    'region_southwest': 0,
    'bmi_category_Obese': 1 if bmi >= 30 else 0
}

# Set correct region column
input_dict[f"region_{region}"] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Add any missing columns (in case)
for col in expected_cols:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to exactly match training
input_df = input_df[expected_cols]

# Convert types just to be safe
input_df = input_df.astype(float)

# Predict
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
