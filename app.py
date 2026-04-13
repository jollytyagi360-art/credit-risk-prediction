import streamlit as st
import requests

st.title("💳 Credit Risk Prediction App")

# Inputs
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
credit_history = st.selectbox("Credit History", [0, 1])
total_income = st.number_input("Total Income")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", [0,1,2,3])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

if st.button("Predict"):

    url = "http://127.0.0.1:8000/predict"

    payload = {
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "credit_history": credit_history,
        "total_income": total_income,
        "gender": gender,
        "married": married,
        "dependents": dependents,
        "education": education,
        "self_employed": self_employed,
        "property_area": property_area
    }

    response = requests.post(url, params=payload)
    result = response.json()

    if result["prediction"] == "Low Risk":
        st.success("✅ Low Risk Customer")
    else:
        st.error("⚠️ High Risk Customer")