from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# model load
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Credit Risk API is running"}

@app.post("/predict")
def predict(
    loan_amount: float,
    loan_term: float,
    credit_history: int,
    total_income: float,
    gender: str,
    married: str,
    dependents: int,
    education: str,
    self_employed: str,
    property_area: str
):

    # feature engineering
    income_loan_ratio = total_income / (loan_amount + 1)
    loan_amount_log = np.log(loan_amount + 1)
    total_income_log = np.log(total_income + 1)

    # encoding
    gender_male = 1 if gender == "Male" else 0
    married_yes = 1 if married == "Yes" else 0
    dependents_1 = 1 if dependents == 1 else 0
    dependents_2 = 1 if dependents == 2 else 0
    dependents_3 = 1 if dependents >= 3 else 0
    education_not_grad = 1 if education == "Not Graduate" else 0
    self_emp_yes = 1 if self_employed == "Yes" else 0
    property_semiurban = 1 if property_area == "Semiurban" else 0
    property_urban = 1 if property_area == "Urban" else 0

    # input array
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

    prediction = model.predict(input_data)[0]

    result = "Low Risk" if prediction == 1 else "High Risk"

    return {
        "prediction": result
    }