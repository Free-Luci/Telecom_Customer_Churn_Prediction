import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('churn_model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

# Page Configuration
st.set_page_config(
    page_title="Telecom Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Telecom Customer Churn Prediction System")

# Description
st.markdown("""
This AI-powered application predicts whether a telecom customer is likely to churn 
based on customer subscription, billing, and service usage behavior.
""")

# Sidebar
st.sidebar.header("ℹ️ How to Use")

st.sidebar.info("""
1. Enter customer details  
2. Click Predict Churn  
3. View prediction results and churn probability  
""")

# About Section
with st.expander("ℹ️ About This Project"):
    st.write("""
    This machine learning project uses customer behavioral data 
    to predict telecom customer churn using a Random Forest Classifier.
    """)

# Customer Information
st.subheader("👤 Customer Information")

tenure = st.slider(
    "Customer Tenure (Months)",
    0,
    72,
    12,
    help="Number of months customer stayed with the company"
)

# Billing Information
st.subheader("💳 Billing Information")

col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=500.0,
        value=70.0
    )

with col2:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

# Service Information
st.subheader("🌐 Service Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-Month", "One Year", "Two Year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber Optic", "No Internet"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

# Encoding
gender_map = {
    "Male": 1,
    "Female": 0
}

contract_map = {
    "Month-to-Month": 0,
    "One Year": 1,
    "Two Year": 2
}

internet_map = {
    "DSL": 0,
    "Fiber Optic": 1,
    "No Internet": 2
}

tech_support_map = {
    "Yes": 1,
    "No": 0
}

# Encoded Values
Gender = gender_map[gender]
ContractType = contract_map[contract]
InternetService = internet_map[internet_service]
TechSupport = tech_support_map[tech_support]

# Create Input DataFrame
input_data = pd.DataFrame([[
    30,  # Age default
    Gender,
    tenure,
    monthly_charges,
    ContractType,
    InternetService,
    total_charges,
    TechSupport
]], columns=[
    'Age',
    'Gender',
    'Tenure',
    'MonthlyCharges',
    'ContractType',
    'InternetService',
    'TotalCharges',
    'TechSupport'
])

# Match model columns
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict Churn"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )

    if prediction == 1:

        st.error("⚠️ High Churn Risk Detected")

        st.write("""
        This customer shows behavior patterns commonly associated with churn:
        - Short customer tenure
        - Higher monthly billing
        - Flexible contract plans
        """)

    else:

        st.success("✅ Customer Likely to Stay")

        st.write("""
        This customer shows stable subscription behavior and lower churn risk.
        """)

# Footer
st.markdown("---")

st.caption(
    "Built using Machine Learning, Scikit-learn, and Streamlit"
)