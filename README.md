# Credit Risk AI 🇺🇸🇦🇺

**AI-powered credit risk scoring system for financial transparency and national interest.**

---

## 🎯 Project Goals

- Reduce systemic financial risk through AI-driven credit scoring
- Support underserved populations with alternative data
- Align with national interest priorities for NIW/NIV migration
- Provide scalable, secure, and interpretable models for US and Australian financial institutions

---

## 🧠 Key Features

- Predictive modeling using ML/DL (XGBoost, LightGBM, PyTorch)
- Integration of alternative data (non-traditional financial signals)
- REST API for banking systems and credit platforms
- Interactive dashboard for financial analysts and regulators
- Bilingual documentation (English & Persian)
- Fully Dockerized and CI/CD-enabled for secure deployment

---

## 🛠 Tech Stack

| Layer        | Tools & Libraries                  |
|--------------|------------------------------------|
| Language     | Python 3.11+                       |
| ML Models    | XGBoost, LightGBM, PyTorch         |
| API          | FastAPI                            |
| Dashboard    | Streamlit                          |
| CI/CD        | GitHub Actions, Docker             |
| Security     | SSH, JWT, HTTPS                    |

---

## 📦 Project Structure
credit-risk-ai/ ├── data/                   # Raw and processed datasets ├── notebooks/              # Jupyter notebooks for EDA and prototyping ├── src/ │   ├── data_preprocessing/ # Feature engineering and cleaning │   ├── models/             # ML/DL models and training scripts │   ├── api/                # FastAPI endpoints │   └── dashboard/          # Streamlit dashboard code ├── tests/                  # Unit and integration tests ├── requirements.txt        # Python dependencies ├── Dockerfile              # Containerization setup ├── .github/workflows/      # CI/CD pipelines └── README.md               # Project overview

---

## 🚀 Deployment

To run locally:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn src.api.main:app --reload

# Run dashboard
streamlit run src/dashboard/app.py



🔐 Security Notes
- All secrets and credentials are stored in .env and excluded via .gitignore
- SSH keys are used for CI/CD authentication
- JWT tokens secure API endpoints
- HTTPS enforced in production

📄 License
MIT License

👤 Author
Mohammad Yadollah Moghadam
Banking Expert & Web Developer | Maskan Bank
GitHub: mym1359
LinkedIn: mym1980

🇮🇷 نسخه فارسی
این پروژه با هدف کاهش ریسک سیستماتیک مالی و شفاف‌سازی اعتبارسنجی طراحی شده است. با استفاده از هوش مصنوعی و داده‌های جایگزین، امکان ارزیابی دقیق‌تر متقاضیان وام فراهم می‌شود. این سیستم می‌تواند به عنوان یک ابزار ملی در آمریکا و استرالیا مورد استفاده قرار گیرد و در پرونده مهاجرت تخصصی (NIW/NIV) نقش کلیدی ایفا کند.

