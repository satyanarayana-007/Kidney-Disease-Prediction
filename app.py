import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("Best_Kidney_Model.pkl")
scaler = joblib.load("Scaler.pkl")

st.title("Kidney Disease Prediction")

st.write("Enter Patient Details")

# Create input fields
Age = st.number_input("Age", 1, 120)
Gender = st.selectbox("Gender", [0,1])

BMI = st.number_input("BMI", 10.0,60.0)

Creatinine = st.number_input("Creatinine",0.0,20.0)

BUN = st.number_input("Blood Urea Nitrogen",0.0,100.0)

GFR = st.number_input("GFR",0.0,150.0)

Protein = st.number_input("Protein in Urine",0.0,10.0)

BloodPressure = st.number_input("Blood Pressure",50.0,220.0)

# Add ALL remaining features in the same order as the dataset

if st.button("Predict"):

    input_data = pd.DataFrame([[

        Age,
        Gender,
        BMI,
        Creatinine,
        BUN,
        GFR,
        Protein,
        BloodPressure

        # Remaining Features...

    ]], columns=[

        "Age",
        "Gender",
        "BMI",
        "Creatinine",
        "BUN",
        "GFR",
        "ProteinInUrine",
        "BloodPressure"

        # Remaining column names...

    ])

    prediction = model.predict(input_data)

    if prediction[0]==1:
        st.error("Kidney Disease Detected")
    else:
        st.success("No Kidney Disease")