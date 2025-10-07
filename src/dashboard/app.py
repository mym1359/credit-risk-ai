# src/dashboard/app.py

import streamlit as st
import pandas as pd
import xgboost as xgb

# بارگذاری مدل
model = xgb.XGBClassifier()
model.load_model("src/models/base_model.json")

st.set_page_config(page_title="Credit Risk Dashboard", layout="centered")
st.title("🧠 اعتبارسنجی هوشمند مهاجرتی")

st.markdown("مدل اعتبارسنجی بر اساس داده‌های جمعیتی و اقتصادی ایالت‌های آمریکا و استرالیا")

# فرم ورودی
with st.form("risk_form"):
    unemployment = st.slider("نرخ بیکاری", 0.0, 20.0, 5.0)
    poverty = st.slider("نرخ فقر", 0.0, 30.0, 15.0)
    submitted = st.form_submit_button("محاسبه اعتبار")

if submitted:
    df = pd.DataFrame([{
        "UnemploymentRate": unemployment,
        "PovertyRate": poverty
    }])
    prediction = model.predict(df)[0]
    risk = "ریسک پایین ✅" if prediction == 1 else "ریسک بالا ⚠️"
    st.success(f"نتیجه اعتبارسنجی: {risk}")