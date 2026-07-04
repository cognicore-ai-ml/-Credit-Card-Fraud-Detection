import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Streamlit UI
st.title("💳 Credit Card Fraud Detection")
st.write("Upload a CSV file with transaction data to get fraud predictions.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read uploaded data
    data = pd.read_csv(uploaded_file)

    # Make predictions
    predictions = model.predict(data)

    # Add predictions to dataframe
    data["Fraud Prediction"] = predictions

    # Display results
    st.write("📊 Prediction Results:")
    st.dataframe(data)
