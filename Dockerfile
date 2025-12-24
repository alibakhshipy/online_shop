FROM python:3.13-slim

WORKDIR /app

# نصب dependencies سیستم
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# کپی requirements و نصب پکیج‌ها
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# کپی بقیه فایل‌ها
COPY . .

# اجرای migrations و collectstatic
RUN python manage.py collectstatic --noinput

# پورت اکسپوز
EXPOSE 8000

# دستور اجرا
CMD ["gunicorn", "djangoProject.wsgi:application", "--bind", "0.0.0.0:8000"]