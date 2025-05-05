# dashboard/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Demand Forecasting", layout="centered")

st.title("📦 Product Demand Forecasting")
st.markdown("Enter lag values to predict future sales:")

lag_1 = st.number_input("Sales 1 day ago (lag_1)", value=300.0)
lag_7 = st.number_input("Sales 7 days ago (lag_7)", value=250.0)

if st.button("🔮 Predict Sales"):
    input_data = {
        "lag_1": lag_1,
        "lag_7": lag_7
    }
    try:
        response = requests.post("http://127.0.0.1:8000/predict/", json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"📈 Predicted Sales: **{result['predicted_sales']:.2f}**")
        else:
            st.error("⚠️ Failed to get prediction from API")
    except Exception as e:
        st.error(f"❌ Error: {e}")
