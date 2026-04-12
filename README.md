# 💳 Credit Risk Prediction App

🚀 Live App: https://credit-risk-prediction-hssajzo9xv9scmcwqsdl2l.streamlit.app

---

## 📌 Business Problem

Financial institutions face a major challenge in identifying whether a loan applicant is likely to **default (High Risk)** or **repay (Low Risk)**.

Incorrect decisions can lead to:
- High financial losses  
- Increased non-performing assets (NPAs)  
- Inefficient credit allocation  

👉 The goal of this project is to build a **machine learning solution** that helps banks **assess credit risk before loan approval**.

---

## 🎯 Objective

To develop a predictive model that classifies applicants into:

- ✅ Low Risk (Safe to approve loan)  
- ⚠️ High Risk (Potential default risk)  

---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit (Deployment)  

---

## 🧠 Machine Learning Approach

### 1. Data Preprocessing
- Handling missing values  
- Encoding categorical variables  
- Feature scaling  

---

### 2. Feature Engineering
- Income + Co-applicant income → **Total Income**  
- Created **Income-Loan Ratio**  
- Applied **log transformation** to reduce skewness  

---

### 3. Model Building

Trained and compared multiple models:

- Logistic Regression (Baseline)  
- Random Forest  
- XGBoost (Best performance)  

---

### 4. Model Evaluation

- Accuracy comparison  
- Generalization on test data  
- Selection based on performance & stability  

---

### 5. Deployment

- Built interactive UI using **Streamlit**  
- Integrated trained model (`model.pkl`)  
- Deployed on **Streamlit Cloud**  

---

## 📊 Key Features

- Real-time prediction via UI  
- Handles both numerical & categorical inputs  
- Feature engineering for better accuracy  
- Model comparison for optimal performance  
- End-to-end ML pipeline deployment  

---

## 🧪 Input Features

- Loan Amount  
- Loan Term  
- Credit History  
- Total Income  
- Gender  
- Married  
- Dependents  
- Education  
- Self Employed  
- Property Area  

---

## 📈 Output

- ✅ Low Risk Customer  
- ⚠️ High Risk Customer  

---

## 🖥️ How to Run Locally

```bash
git clone https://github.com/jollytyagi360-art/credit-risk-prediction.git
cd credit-risk-prediction
pip install -r requirements.txt
streamlit run app.py
