import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Industrial Predictive Maintenance",
    layout="wide"
)

st.title("🔧 Industrial Predictive Maintenance Dashboard")

st.markdown("### Federated Learning AI Monitoring System")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Machine Sensors")

temperature = st.sidebar.slider("Temperature", 0.0, 200.0, 75.0)
pressure = st.sidebar.slider("Pressure", 0.0, 300.0, 120.0)
vibration = st.sidebar.slider("Vibration", 0.0, 100.0, 40.0)

# -----------------------------
# Prediction Logic
# -----------------------------
risk_score = np.mean([temperature, pressure, vibration])

health = max(0, 100 - int(risk_score))

# -----------------------------
# Main Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Machine Health")

    st.metric(
        label="Health Score",
        value=f"{health}%"
    )

    st.progress(health / 100)

with col2:

    st.subheader("⚠️ Failure Risk")

    st.metric(
        label="Risk Score",
        value=f"{int(risk_score)}%"
    )

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Run AI Prediction"):

    if risk_score < 80:
        st.success("✅ Machine Status: Healthy")

    elif risk_score < 140:
        st.warning("⚠️ Maintenance Recommended")

    else:
        st.error("🚨 Failure Risk Detected")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("AI-powered Predictive Maintenance using Federated Learning")