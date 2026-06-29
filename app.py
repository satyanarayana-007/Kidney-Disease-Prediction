import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("Best_Kidney_Model.pkl")
scaler = joblib.load("Scaler.pkl")

st.title("🩺 Kidney Disease Prediction")

st.write("Enter Patient Details")

# --------------------------
# Input Fields
# --------------------------

Age = st.number_input("Age", 1, 120)

Gender = st.selectbox("Gender", [0, 1])

BMI = st.number_input("BMI", 10.0, 60.0)

SystolicBP = st.number_input("Systolic Blood Pressure", 70, 250)

DiastolicBP = st.number_input("Diastolic Blood Pressure", 40, 150)

SerumCreatinine = st.number_input("Serum Creatinine", 0.0, 20.0)

BUNLevels = st.number_input("BUN Levels", 0.0, 100.0)

GFR = st.number_input("GFR", 0.0, 150.0)

ProteinInUrine = st.number_input("Protein In Urine", 0.0, 10.0)

HbA1c = st.number_input("HbA1c", 3.0, 15.0)

# --------------------------
# Prediction
# --------------------------

if st.button("Predict"):

    input_data = pd.DataFrame([[
        Age,
        Gender,
        BMI,
        SystolicBP,
        DiastolicBP,
        SerumCreatinine,
        BUNLevels,
        GFR,
        ProteinInUrine,
        HbA1c
    ]], columns=[
        "Age",
        "Gender",
        "BMI",
        "SystolicBP",
        "DiastolicBP",
        "SerumCreatinine",
        "BUNLevels",
        "GFR",
        "ProteinInUrine",
        "HbA1c"
    ])

    # Scale input because Logistic Regression was trained on scaled data
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
      import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("Best_Kidney_Model.pkl")
scaler = joblib.load("Scaler.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🩺 Kidney Disease Prediction")
st.write("Enter Patient Details")

# -----------------------------
# Input Fields
# -----------------------------

Age = st.number_input("Age", 1, 120)

Gender = st.selectbox("Gender", [0, 1])

BMI = st.number_input("BMI", 10.0, 60.0)

SystolicBP = st.number_input("Systolic Blood Pressure", 70, 250)

DiastolicBP = st.number_input("Diastolic Blood Pressure", 40, 150)

SerumCreatinine = st.number_input("Serum Creatinine", 0.0, 20.0)

BUNLevels = st.number_input("BUN Levels", 0.0, 100.0)

GFR = st.number_input("GFR", 0.0, 150.0)

ProteinInUrine = st.number_input("Protein In Urine", 0.0, 10.0)

HbA1c = st.number_input("HbA1c", 3.0, 15.0)

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("Predict"):

    input_data = pd.DataFrame([[
        Age,
        Gender,
        BMI,
        SystolicBP,
        DiastolicBP,
        SerumCreatinine,
        BUNLevels,
        GFR,
        ProteinInUrine,
        HbA1c
    ]], columns=[
        "Age",
        "Gender",
        "BMI",
        "SystolicBP",
        "DiastolicBP",
        "SerumCreatinine",
        "BUNLevels",
        "GFR",
        "ProteinInUrine",
        "HbA1c"
    ])

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease Detected")  
        st.error("⚠️ Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease Detected")
