# نمونهٔ آموزشی مدل ریسک اعتباری | Credit Risk AI prototype

این مخزن نمونه‌ای از خط لولهٔ آموزش مدل، API و رابط Streamlit را نشان می‌دهد. کد آموزش نمونه از داده‌های تجمیعی استفاده می‌کند و برچسب آموزشی را از آستانهٔ مجموع نرخ بیکاری و فقر می‌سازد.

This repository demonstrates a model-training pipeline, an API, and a Streamlit interface. The example trainer uses aggregate data and constructs an illustrative label from a threshold on unemployment and poverty rates.

## اجزای مخزن | Repository components

- [آموزش مدل / Model training](src/models/base_model.py)
- [رابط API / API](src/api/main.py)
- [رابط Streamlit / Streamlit interface](src/dashboard/app.py)
- [آزمون API / API test](tests/test_api.py)

## تفسیر | Interpretation

امتیازهای این تمرین نشان می‌دهند مدل تا چه حد می‌تواند برچسب ساخته‌شده از ورودی‌های خودش را بازتولید کند. دادهٔ پیامد بازپرداخت در سطح فرد، اعتبارسنجی منصفانه برای متقاضیان، و آزمون آمادگی تولید در این نمونه گزارش نشده‌اند. فعالیت خودکار مخزن نیز بخشی از کار آزمایشی GitHub Actions است.

Scores in this exercise measure how well the model reproduces a label derived from its inputs. This repository does not report borrower-level repayment outcomes, fairness validation for applicants, or production readiness testing. Scheduled repository activity is a GitHub Actions demonstration.

[پژوهش بازپرداخت وام مسکن / Mortgage repayment research](https://github.com/mym1359/mortgage-repayment-review)
