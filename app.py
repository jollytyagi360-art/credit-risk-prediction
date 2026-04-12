import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("💳 Credit Risk Prediction App")

st.write("Enter customer details:")

# Basic inputs
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
credit_history = st.selectbox("Credit History (0 = Bad, 1 = Good)", [0, 1])
total_income = st.number_input("Total Income")

# Derived inputs
income_loan_ratio = total_income / loan_amount if loan_amount != 0 else 0
loan_amount_log = np.log(loan_amount + 1)
total_income_log = np.log(total_income + 1)

# Categorical inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding
gender_male = 1 if gender == "Male" else 0
married_yes = 1 if married == "Yes" else 0
dependents_1 = 1 if dependents == "1" else 0
dependents_2 = 1 if dependents == "2" else 0
dependents_3 = 1 if dependents == "3+" else 0
education_not_grad = 1 if education == "Not Graduate" else 0
self_emp_yes = 1 if self_employed == "Yes" else 0
property_semiurban = 1 if property_area == "Semiurban" else 0
property_urban = 1 if property_area == "Urban" else 0

# Prediction
if st.button("Predict"):

    input_data = np.array([[ 
        loan_amount,
        loan_term,
        credit_history,
        total_income,
        income_loan_ratio,
        loan_amount_log,
        total_income_log,
        gender_male,
        married_yes,
        dependents_1,
        dependents_2,
        dependents_3,
        education_not_grad,
        self_emp_yes,
        property_semiurban,
        property_urban
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Low Risk Customer ✅")
    else:
        st.error("High Risk Customer ⚠️")