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

# Preprocessing user input
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

# Optional BMI Category
if bmi >= 30:
    input_dict['bmi_category_Obese'] = 1
else:
    input_dict['bmi_category_Obese'] = 0

# Predict and show result
if st.button("Predict Insurance Cost"):
    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Enforce correct data types for each column
    input_df = input_df.astype({
        'age': 'int',
        'sex': 'int',
        'bmi': 'float',
        'children': 'int',
        'smoker': 'int',
        'region_northwest': 'int',
        'region_southeast': 'int',
        'region_southwest': 'int',
        'bmi_category_Obese': 'int'
    })

    # Ensure all required columns are present
    required_cols = ['age', 'sex', 'bmi', 'children', 'smoker',
                     'region_northwest', 'region_southeast', 'region_southwest',
                     'bmi_category_Obese']

    for col in required_cols:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match training order
    input_df = input_df[required_cols]

    # (Optional) Debug info
    # st.write("Input shape:", input_df.shape)
    # st.write(input_df.head())

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")
