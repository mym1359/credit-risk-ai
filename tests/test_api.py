import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://127.0.0.1:8000"
USERNAME = os.getenv("ADMIN_USERNAME", "admin")
PASSWORD = os.getenv("ADMIN_PASSWORD", "password123")

def test_login_success():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(f"{BASE_URL}/token", data=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure():
    payload = {
        "username": USERNAME,
        "password": "wrongpassword"
    }
    response = requests.post(f"{BASE_URL}/token", data=payload)
    assert response.status_code == 401

def test_predict_with_valid_token():
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    token_response = requests.post(f"{BASE_URL}/token", data=login_payload)
    assert token_response.status_code == 200
    token = token_response.json().get("access_token")
    assert token is not None

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "unemployment_rate": 5.0,
        "poverty_rate": 15.0
    }
    response = requests.post(f"{BASE_URL}/predict/", json=payload, headers=headers)
    assert response.status_code == 200
    assert "risk_level" in response.json()

def test_predict_with_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken123"}
    payload = {
        "unemployment_rate": 5.0,
        "poverty_rate": 15.0
    }
    response = requests.post(f"{BASE_URL}/predict/", json=payload, headers=headers)
    assert response.status_code == 401

def test_predict_with_missing_fields():
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    token_response = requests.post(f"{BASE_URL}/token", data=login_payload)
    assert token_response.status_code == 200
    token = token_response.json().get("access_token")
    assert token is not None

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "unemployment_rate": 5.0  # فیلد poverty_rate حذف شده
    }
    response = requests.post(f"{BASE_URL}/predict/", json=payload, headers=headers)
    assert response.status_code == 422