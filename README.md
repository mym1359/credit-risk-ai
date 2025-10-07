 README Content (English Version)
# 🧠 Credit Risk AI – Migration-Ready and Deployable

An intelligent credit scoring project based on demographic data from the United States and Australia, designed to showcase technical expertise in banking, AI, and global deployment for professional and migration purposes.

---

## 🚀 Features

- Credit scoring model using XGBoost based on public data
- FastAPI-powered REST API for real-time scoring
- Interactive dashboard built with Streamlit
- Dockerized for professional deployment
- Ready for CI/CD integration via GitHub Actions

---

## 📊 Data Sources

- `us_census_2021.csv`: Unemployment and poverty rates by U.S. state
- `aus_population_stats.csv`: Equivalent data for Australian states and territories

---

## 🧠 Model

- Algorithm: XGBoost
- Features: Unemployment rate, Poverty rate
- Output: Credit risk classification (Low Risk / High Risk)

---

## 🔌 API

- Endpoint: `/predict/`
- Input:
  ```json
  {
    "unemployment_rate": 4.2,
    "poverty_rate": 13.8
  }


- Output:
{
  "prediction": 1,
  "risk_level": "Low Risk"
}



📺 Dashboard
- Run Streamlit:
streamlit run src/dashboard/app.py
- Features:
- Interactive form for inputting unemployment and poverty rates
- Real-time credit risk prediction
- Extendable with charts, maps, and country comparisons

🐳 Docker
- Build container:
docker build -t credit-risk-api .
- Run API in container:
docker run -p 8000:8000 credit-risk-api
- Access API:
http://localhost:8000/docs



📦 Project Structure
credit-risk-ai/
├── data/
│   ├── us_census_2021.csv
│   └── aus_population_stats.csv
├── src/
│   ├── models/
│   │   └── base_model.py
│   ├── api/
│   │   └── main.py
│   └── dashboard/
│       └── app.py
├── Dockerfile
├── requirements.txt
└── README.md



✈️ Migration Purpose
This project supports professional migration to the United States and Australia by demonstrating:
- AI and banking domain expertise
- End-to-end project design and deployment
- Technical documentation and global readiness
- Real-world application of credit scoring logic

👨‍💻 Developer
Mohammad Yadollah Moghadam
Banking Expert & Web Developer at Maskan Bank
📍 Iran
🌐 GitHub: github.com/mym1359

📢 License & Usage
This project is intended for educational, migration, and professional demonstration purposes. Commercial or banking use requires permission from the original developer.
