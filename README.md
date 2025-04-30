# 💰 Healthcare Insurance Cost Predictor

A complete end-to-end **Machine Learning + Streamlit** project that predicts a person's **annual health insurance premium** based on demographic and health-related inputs.

> 🧠 Uses Random Forest Regression trained on the Medical Cost Personal Dataset  
> 🚀 Deployed via Streamlit | 📓 Built and tested in Jupyter Notebook

---

## 🔗 Live App

👉 [Try the App on Streamlit](https://healthcare-insurance-app2.streamlit.app)

---

## 📘 Project Overview

This project predicts **annual insurance charges** using inputs such as:
- Age, Gender, BMI
- Number of Children
- Smoking status
- Residential Region

It covers data exploration, feature engineering, model training, and a deployed web interface.

---

## 📊 Sample Visualizations

### 📈 Children vs Charges (Boxplot)
![Children vs Charges](https://github.com/krishnatejakotla/healthcare-insurance-streamlit-app/blob/main/children_vs_charges.png?raw=true)

### 📊 Feature Importance (Random Forest)
![Feature Importance](https://github.com/krishnatejakotla/healthcare-insurance-streamlit-app/blob/main/feature_importance.png?raw=true)

📓 Full notebook with charts: [Healthcare_Insurance_Cost_Prediction.ipynb](Healthcare_Insurance_Cost_Prediction.ipynb)

---

## 🧠 Features

- Predicts insurance cost using a trained Random Forest model
- Feature importance analysis
- Handles categorical variables and BMI-based obesity classification
- Interactive Streamlit UI

---

## 🛠 Technologies Used

- Python
- Pandas, NumPy
- scikit-learn (Random Forest Regressor)
- Seaborn & Matplotlib
- Streamlit (App deployment)
- Jupyter Notebook

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `insurance.csv` | Original dataset |
| `Healthcare_Insurance_Cost_Prediction.ipynb` | Notebook with EDA + model training |
| `model.pkl` | Trained ML model |
| `app.py` | Streamlit app code |
| `requirements.txt` | Project dependencies |
| `children_vs_charges.png` | Chart: Children vs Charges |
| `feature_importance.png` | Chart: Feature Importance |


## 🚀 Run Locally

bash
git clone https://github.com/krishnatejakotla/healthcare-insurance-streamlit-app.git
cd healthcare-insurance-streamlit-app
pip install -r requirements.txt
streamlit run app.py


## 📌 Notes

- The predicted insurance cost is **annual** and based on demographic and health-related features.
- Real-world charges may vary depending on insurance provider and region.
- **Problems faced during development:**
  - Initial model prediction failed due to mismatched input columns.
  - Encountered `ValueError` from missing encoded features (e.g., regions, smoker status).
  - Fixed by explicitly aligning input features in Streamlit with model training features.
  - Streamlit app didn’t display uploaded chart images until filenames were corrected.
- **Learnings:**
  - Improved understanding of regression workflows, feature importance, and app deployment.
  - Gained hands-on experience troubleshooting model and deployment issues.
- This project is for educational purposes only and not intended for real underwriting.

---

## 👨‍💻 Author

**Krishna Teja Reddy Kotla**  
🎓 Master's in Management Information Systems  
📍 Auburn University at Montgomery  
📊 Data Analytics & Business Intelligence Enthusiast  
🛠️ Skilled in Python, SQL, Power BI, Tableau, scikit-learn, and Streamlit  
🔗 [LinkedIn](https://www.linkedin.com/in/krishnatejakotla/) | [GitHub](https://github.com/krishnatejakotla)


