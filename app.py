import streamlit as st
import joblib
import numpy as np

# Load the saved model and label encoder
model = joblib.load("mental_health_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🧠 Mental Health Prediction for Students")

# Input fields
hours_studied = st.slider("Hours Studied per Day", 0.0, 10.0, 2.0)
sleep_hours = st.slider("Sleep Hours", 3.0, 10.0, 6.0)
social_media = st.slider("Social Media Usage (hrs/day)", 0.0, 6.0, 2.0)
exercise = st.radio("Do You Exercise Daily?", ['Yes', 'No'])
water_intake = st.slider("Water Intake (litres/day)", 0.5, 4.0, 2.0)
internal_marks = st.slider("Internal Marks (out of 30)", 0, 30, 15)
family_support = st.slider("Family Support (1-5)", 1, 5, 3)

# Convert inputs
exercise_bin = 1 if exercise == 'Yes' else 0
features = np.array([[hours_studied, sleep_hours, social_media, exercise_bin,
                      water_intake, internal_marks, family_support]])

if st.button("Predict Stress Level"):
    prediction = model.predict(features)[0]
    stress_label = label_encoder.inverse_transform([prediction])[0]
    st.success(f"🧠 Predicted Stress Level: **{stress_label}**")
