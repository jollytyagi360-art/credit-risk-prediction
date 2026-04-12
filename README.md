# 💳 Credit Risk Prediction App

🚀 Live App: https://credit-risk-prediction-hssajzo9xv9scmcwqsdl2l.streamlit.app  

💻 GitHub Repository:  
https://github.com/jollytyagi360-art/credit-risk-prediction  

🎬 Demo Video:  
👉 https://www.linkedin.com/posts/nishant-tyagi-7aa458356_machinelearning-datascience-python-activity-7449094279098167296-lXfT

---

## 📌 Business Problem

Financial institutions need to decide whether a loan applicant is likely to repay or default.  
Wrong decisions can lead to financial losses, increased NPAs, and poor risk management.

👉 This project solves that problem by predicting whether a customer is **High Risk or Low Risk** before loan approval.

---

## 🎯 Objective

To build a machine learning model that classifies applicants into:

- ✅ Low Risk (Safe to approve)  
- ⚠️ High Risk (Potential default)  

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
- Handled missing values  
- Encoded categorical variables  
- Scaled numerical features  

---

### 2. Feature Engineering
- Created **Total Income**  
- Created **Income-Loan Ratio**  
- Applied **log transformation**  

---

### 3. Model Building

Trained multiple models:

- Logistic Regression  
- Random Forest  
- XGBoost  

---

### 4. Model Evaluation

- Compared model performance  
- Selected best model based on accuracy  

---

### 5. Deployment

- Built UI using Streamlit  
- Integrated trained model  
- Deployed on Streamlit Cloud  

---

## 📊 Model Performance

- Logistic Regression → ~78% accuracy  
- Random Forest → ~81% accuracy  
- XGBoost → ~79% accuracy  

👉 Random Forest performed best overall.

---

## 📌 Key Insights

- Credit History is the most important feature  
- High loan + low income increases risk  
- Feature engineering improved accuracy  
- Tree-based models outperformed linear models  

---

## 📊 Input Features

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

## 🖥️ Run Locally

```bash
git clone https://github.com/jollytyagi360-art/credit-risk-prediction.git
cd credit-risk-prediction
pip install -r requirements.txt
streamlit run app.py
