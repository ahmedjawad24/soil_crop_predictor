import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and label encoder
model = joblib.load("random_forest_crop_regression.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Streamlit UI
st.title("🌾 Crop Recommendation System (Regression Based)")
st.write("Enter soil parameters to get the recommended crop.")

# User input sliders
n = st.slider("Nitrogen (N)", 0, 250, 100)
p = st.slider("Phosphorous (P)", 0, 120, 50)
k = st.slider("Potassium (K)", 0, 120, 50)
ph = st.slider("pH", 4.0, 9.0, 6.5)

# Predict crop
if st.button("Predict Crop"):
    input_data = np.array([[n, p, k, ph]])
    prediction = model.predict(input_data)[0]
    predicted_class = int(np.round(prediction))
    predicted_class = np.clip(predicted_class, 0, len(label_encoder.classes_) - 1)
    crop_name = label_encoder.inverse_transform([predicted_class])[0]

    st.success(f"✅ Recommended Crop: **{crop_name}**")
