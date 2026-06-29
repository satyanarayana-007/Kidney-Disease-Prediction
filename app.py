import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model and Scaler
# -----------------------------
model = joblib.load("Best_Kidney_Model.pkl")
scaler = joblib.load("Scaler.pkl")

st.set_page_config(page_title="Kidney Disease Prediction", page_icon="🩺")

st.title("🩺 Kidney Disease Prediction System")
st.write("Enter the patient's details below.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

Age = st.number_input("Age", 1, 120, 30)

Gender = st.selectbox(
    "Gender",
    [0, 1],
    format_func=lambda x: "Male" if x == 1 else "Female"
)

BMI = st.number_input("BMI", 10.0, 60.0, 25.0)

SystolicBP = st.number_input("Systolic Blood Pressure", 70, 250, 120)

DiastolicBP = st.number_input("Diastolic Blood Pressure", 40, 150, 80)

SerumCreatinine = st.number_input("Serum Creatinine", 0.0, 20.0, 1.0)

BUNLevels = st.number_input("BUN Levels", 0.0, 100.0, 15.0)

GFR = st.number_input("GFR", 0.0, 200.0, 90.0)

ProteinInUrine = st.number_input("Protein in Urine", 0.0, 10.0, 0.2)

HbA1c = st.number_input("HbA1c", 3.0, 15.0, 5.5)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    input_data = pd.DataFrame({

        "Age":[Age],
        "Gender":[Gender],
        "BMI":[BMI],
        "SystolicBP":[SystolicBP],
        "DiastolicBP":[DiastolicBP],
        "SerumCreatinine":[SerumCreatinine],
        "BUNLevels":[BUNLevels],
        "GFR":[GFR],
        "ProteinInUrine":[ProteinInUrine],
        "HbA1c":[HbA1c]

    })

    # Scale Input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease Detected")

    st.write("### Prediction Probability")

    st.write(f"Healthy : {probability[0][0]*100:.2f}%")

    st.write(f"Kidney Disease : {probability[0][1]*100:.2f}%")
