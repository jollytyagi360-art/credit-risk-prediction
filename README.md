# 💳 Credit Risk Prediction System

🚀 **Live App (Frontend):**
https://credit-risk-prediction-hssajzo9xv9scmcwqsdl2l.streamlit.app

⚡ **Live API (Backend):**
https://credit-risk-prediction-wc7k.onrender.com

📄 **API Docs (Swagger UI):**
https://credit-risk-prediction-wc7k.onrender.com/docs

💻 **GitHub Repository:**
https://github.com/jollytyagi360-art/credit-risk-prediction

🎬 **Demo Video:**
https://www.linkedin.com/posts/nishant-tyagi-7aa458356_machinelearning-datascience-python-activity-7449094279098167296-lXfT

---

# 📌 Business Problem

Financial institutions must decide whether a loan applicant is likely to repay or default.

Incorrect decisions lead to:

* Financial losses
* Increased NPAs (Non-Performing Assets)
* Poor risk management

👉 This project solves the problem by predicting whether a customer is **High Risk or Low Risk** before loan approval.

---

# 🎯 Objective

To build a **production-level machine learning system** that classifies applicants into:

* ✅ Low Risk (Safe to approve)
* ⚠️ High Risk (Potential default)

---

# 🏗️ System Architecture

Frontend (Streamlit) → API (FastAPI) → ML Model

👉 Clean separation between UI and backend makes the system scalable and production-ready.

---

# ⚙️ Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn
* XGBoost
* FastAPI (Backend API)
* Streamlit (Frontend UI)
* Render (API Deployment)
* Streamlit Cloud (Frontend Deployment)

---

# 🧠 Machine Learning Approach

## 1. Data Preprocessing

* Handled missing values
* Encoded categorical variables
* Scaled numerical features

---

## 2. Feature Engineering

* Created **Total Income**
* Created **Income-Loan Ratio**
* Applied **log transformation**

---

## 3. Model Building

Trained multiple models:

* Logistic Regression
* Random Forest
* XGBoost

---

## 4. Model Evaluation

* Compared model performance
* Selected best model based on accuracy

---

## 5. Deployment

* Built frontend using Streamlit
* Created REST API using FastAPI
* Deployed backend on Render
* Connected frontend with live API

---

# 📊 Model Performance

* Logistic Regression → ~78% accuracy
* Random Forest → ~81% accuracy ⭐
* XGBoost → ~79% accuracy

👉 **Random Forest performed best overall**

---

# 📌 Key Insights

* Credit History is the most important feature
* High loan + low income increases default risk
* Feature engineering improved model performance
* Tree-based models outperformed linear models

---

# 📊 Input Features

* Loan Amount
* Loan Term
* Credit History
* Total Income
* Gender
* Married
* Dependents
* Education
* Self Employed
* Property Area

---

# 📈 Output

* ✅ Low Risk Customer
* ⚠️ High Risk Customer

---

# 🔌 API Usage

### Endpoint:

POST /predict

### Example Request:

```json
{
  "loan_amount": 120,
  "loan_term": 360,
  "credit_history": 1,
  "total_income": 5000,
  "gender": "Male",
  "married": "Yes",
  "dependents": 1,
  "education": "Graduate",
  "self_employed": "No",
  "property_area": "Urban"
}
```

### Response:

```json
{
  "prediction": "Low Risk"
}
```

---

# 🖥️ Run Locally

```bash
git clone https://github.com/jollytyagi360-art/credit-risk-prediction.git
cd credit-risk-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

# 📸 Demo

🎬 Watch Demo Video:
https://www.linkedin.com/posts/nishant-tyagi-7aa458356_machinelearning-datascience-python-activity-7449094279098167296-lXfT

---

# 📌 Business Impact

* Helps reduce loan defaults
* Improves decision-making
* Automates credit risk assessment
* Saves manual effort for banks

---

# 📊 Conclusion

* Machine Learning improves credit risk prediction
* Random Forest delivered best performance
* Feature engineering played a critical role
* Built a complete end-to-end ML system

---

# 🚀 Future Improvements

* Add risk probability (%)
* Improve UI/UX
* Add user authentication
* Docker containerization
* Cloud deployment (AWS/GCP)

---

# 👨‍💻 Author

**Nishant Tyagi**

---

⭐ If you found this project useful, consider giving it a star!
