# src/models/base_model.py

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data():
    us_df = pd.read_csv("data/us_census_2021.csv")
    aus_df = pd.read_csv("data/aus_population_stats.csv")

    # اضافه کردن ستون کشور
    us_df["Country"] = "USA"
    aus_df["Country"] = "Australia"

    # ترکیب داده‌ها
    df = pd.concat([us_df, aus_df], ignore_index=True)

    # تبدیل داده‌ها به عددی
    df["UnemploymentRate"] = pd.to_numeric(df["UnemploymentRate"], errors="coerce")
    df["PovertyRate"] = pd.to_numeric(df["PovertyRate"], errors="coerce")

    # حذف داده‌های ناقص
    df.dropna(inplace=True)

    # ساخت ویژگی‌ها و هدف فرضی (مثلاً اعتبارسنجی خوب یا بد)
    df["CreditRisk"] = (df["UnemploymentRate"] + df["PovertyRate"] < 20).astype(int)

    X = df[["UnemploymentRate", "PovertyRate"]]
    y = df["CreditRisk"]

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    X_train, X_test, y_train, y_test = load_data()
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Model trained with accuracy: {acc:.2f}")
    return model

if __name__ == "__main__":
    model = train_model()
    model.save_model("src/models/base_model.json")