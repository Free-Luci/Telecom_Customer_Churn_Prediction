# 📊 Telecom Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, billing information, and service usage behavior.

---

# 🚀 Live Demo

🔗 Streamlit App:  
https://your-streamlit-app-link.streamlit.app

---

# 📌 Project Overview

Customer churn prediction is one of the most important business problems in the telecom industry. This project uses Machine Learning algorithms to analyze customer behavior and predict whether a customer is likely to leave the telecom service.

The project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Streamlit Web Application Deployment

---

# 🧠 Machine Learning Models Used

The following classification models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)

Among all tested models, the SVC model achieved the highest accuracy and was selected as the final deployment model.

---

# 📂 Dataset Information

Dataset used: Telecom Customer Churn Dataset

The dataset contains customer-related information such as:

- Customer demographics
- Contract type
- Internet service
- Billing information
- Monthly charges
- Total charges
- Tech support
- Churn status

Target Variable:

- Churn
  - Yes → Customer left
  - No → Customer stayed

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

# 📊 Exploratory Data Analysis

The project includes several visualizations such as:

- Churn Distribution Pie Chart
- Monthly Charges Distribution Histogram
- Monthly Charges vs Churn
- Tenure vs Churn
- Confusion Matrix Heatmap

These visualizations helped identify patterns affecting customer churn behavior.

---

# ⚙️ Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Encoding
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Best Model
   ↓
Streamlit Deployment

📈 Model Evaluation Metrics

The models were evaluated using:

Accuracy
Precision
Recall
F1-Score
🏆 Conclusions
SVC achieved the highest performance among all tested models.
Customer tenure, monthly charges, and contract type significantly affected churn behavior.
Customers with month-to-month contracts showed higher churn probability.
Customers with shorter tenure were more likely to leave the service.
🔮 Future Work
Implement advanced boosting models such as XGBoost and LightGBM
Perform feature engineering and hyperparameter tuning
Add model explainability techniques (SHAP, Feature Importance)
Improve Streamlit dashboard with interactive analytics
📁 Project Structure
telecom-customer-churn-prediction/
│
├── app.py
├── churn_model.pkl
├── model_columns.pkl
├── requirements.txt
├── README.md
└── Telecom_Customer_Churn_Prediction.ipynb
▶️ Run Locally
Clone Repository
git clone https://github.com/your-username/telecom-customer-churn-prediction.git
Move into Project Folder
cd telecom-customer-churn-prediction
Install Dependencies
pip install -r requirements.txt
Run Streamlit App
streamlit run app.py