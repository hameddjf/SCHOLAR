# استفاده از ایمیج رسمی پایتون 3.10 بر پایه دبین
FROM python:3.10-slim-bullseye

# تنظیم متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی فایل‌های مورد نیاز
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# کپی کد پروژه
COPY . .

# اجرای سرور جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]