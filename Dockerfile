# مرحله اول: ساخت محیط backend
FROM python:3.10-slim AS backend

# تنظیم پوشه کاری
WORKDIR /app

# کپی فایل‌های پروژه
COPY requirements.txt .
COPY src/ src/

# نصب وابستگی‌ها
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# باز کردن پورت 8000
EXPOSE 8000

# اجرای API با Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]