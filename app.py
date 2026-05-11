import streamlit as st
import numpy as np

st.set_page_config(page_title="Industrial Predictive Maintenance")

st.title("🔧 Industrial Predictive Maintenance")

st.write("Federated Learning AI Dashboard")

temperature = st.slider("Temperature", 0.0, 200.0, 75.0)
pressure = st.slider("Pressure", 0.0, 300.0, 120.0)
vibration = st.slider("Vibration", 0.0, 100.0, 40.0)

if st.button("Predict"):

    score = np.mean([temperature, pressure, vibration])

    if score < 80:
        st.success("✅ Machine Status: Healthy")

    elif score < 140:
        st.warning("⚠️ Maintenance Recommended")

    else:
        st.error("🚨 Failure Risk Detected")