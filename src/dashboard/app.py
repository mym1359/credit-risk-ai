# src/dashboard/app.py

import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Credit Risk Dashboard", layout="centered")
st.title("🧠 Credit Risk via Secure API")

st.markdown("This dashboard authenticates via JWT and sends data to a FastAPI backend.")

# تابع بررسی اعتبار توکن
def is_token_valid():
    return (
        "jwt_token" in st.session_state and
        "token_expiry" in st.session_state and
        datetime.now() < st.session_state["token_expiry"]
    )

# پاک‌سازی توکن منقضی‌شده
if "token_expiry" in st.session_state and datetime.now() > st.session_state["token_expiry"]:
    st.session_state.pop("jwt_token", None)
    st.session_state.pop("token_expiry", None)

# فرم ورود
with st.expander("🔐 Login to get token"):
    username = st.text_input("Username", value="admin")
    password = st.text_input("Password", type="password", value="password123")
    if st.button("Get Token"):
        login_payload = {
            "username": username,
            "password": password
        }
        try:
            token_response = requests.post("http://127.0.0.1:8000/token", data=login_payload)
            token = token_response.json().get("access_token")
            if token:
                st.session_state["jwt_token"] = token
                st.session_state["token_expiry"] = datetime.now() + timedelta(minutes=30)
                st.success("✅ Token received and stored")
            else:
                st.error("❌ Failed to get token")
        except Exception as e:
            st.error(f"Login error: {e}")

# نمایش وضعیت احراز هویت
if is_token_valid():
    st.success("🔐 Authenticated")
else:
    st.warning("🔐 Not authenticated")

# فرم اعتبارسنجی
if is_token_valid():
    with st.form("risk_form"):
        unemployment = st.slider("Unemployment Rate (%)", 0.0, 20.0, 5.0)
        poverty = st.slider("Poverty Rate (%)", 0.0, 30.0, 15.0)
        submitted = st.form_submit_button("Check Credit Risk")

    if submitted:
        payload = {
            "unemployment_rate": unemployment,
            "poverty_rate": poverty
        }
        headers = {
            "Authorization": f"Bearer {st.session_state['jwt_token']}"
        }
        try:
            response = requests.post("http://127.0.0.1:8000/predict/", json=payload, headers=headers)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Risk Level: {result['risk_level']}")
            else:
                st.error(f"❌ API error: {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")
else:
    st.info("🔐 Please login to get a token before using prediction.")