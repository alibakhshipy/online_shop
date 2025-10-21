# 🧾 PROJECT_CHECKLIST.md  
چک‌لیست برای پروژه‌های Django (Template + API)
  
---

## 🔹 فاز 1 – آماده‌سازی اولیه
- [ ] ایجاد ریپوی Git و پوشه پروژه  
- [ ] ایجاد virtualenv و نصب Django + DRF  
- [ ] ساخت فایل requirements.txt  
- [ ] تنظیم فایل .env و .gitignore  
- [ ] ایجاد Dockerfile و docker-compose.yml  
- [ ] تنظیم Postgres / Redis در docker-compose  
- [ ] تست اجرای پروژه در Docker  

---

## 🔹 فاز 2 – ساختاردهی پروژه
- [ ] ایجاد پروژه با django-admin startproject  
- [ ] ساخت فولدر apps و جداسازی تنظیمات (مثلاً settings/base.py, settings/dev.py, settings/prod.py)  
- [ ] تنظیم مسیرهای STATIC و MEDIA در settings  
- [ ] ساخت App اصلی و ثبت در INSTALLED_APPS  

---

## 🔹 فاز 3 – مدل‌سازی
- [ ] پیاده‌سازی مدل User با AbstractBaseUser  
- [ ] ایجاد UserManager و مدل Profile  
- [ ] تعریف Signal برای ساخت خودکار Profile بعد از ساخت User  
- [ ] ایجاد مدل‌های اصلی پروژه (مثل Blog, Post, Comment یا مدل‌های خاص پروژه خودت)  
- [ ] اجرای makemigrations و migrate  
- [ ] تنظیم admin.py برای مدیریت مدل‌ها  

---

## 🔹 فاز 4 – Template و Views
- [ ] تنظیم مسیر Templates و Context Processors  
- [ ] ساخت صفحات HTML پایه (base.html و …)  
- [ ] پیاده‌سازی TemplateView و ListView  
- [ ] ساخت فرم‌های Create / Update / Delete با Class-Based Views  
- [ ] استفاده از LoginRequiredMixin و PermissionRequiredMixin  
- [ ] فعال‌سازی Pagination در ListView  
- [ ] تست نمایش صفحات در مرورگر  

---

## 🔹 فاز 5 – API و RestFramework
- [ ] نصب و راه‌اندازی Django REST Framework  
- [ ] ساخت Serializerها برای مدل‌ها  
- [ ] ایجاد APIView برای CRUD ساده  
- [ ] انتقال به GenericView و ViewSetها  
- [ ] تنظیم Router (DefaultRouter یا SimpleRouter)  
- [ ] اضافه کردن Filtering، Search، Ordering و Pagination  
- [ ] ایجاد Documentation با Swagger یا Redoc  

---

## 🔹 فاز 6 – Authentication API
- [ ] ایجاد endpointهای ثبت‌نام، ورود، خروج  
- [ ] پیاده‌سازی JWT با SimpleJWT  
- [ ] اضافه کردن Email Verification  
- [ ] ارسال ایمیل با SMTP یا Threading  
- [ ] مدیریت Token دستی (فعال‌سازی و بازیابی رمز عبور)  

---

## 🔹 فاز 7 – بهینه‌سازی و تست
- [ ] نصب و تنظیم black و flake8 برای قالب‌بندی و lint  
- [ ] نوشتن تست با TestCase و pytest  
- [ ] تست مدل‌ها، viewها و APIها  
- [ ] ساخت fixture و بررسی coverage  

---

## 🔹 فاز 8 – Background Tasks
- [ ] نصب و تنظیم Redis در Docker  
- [ ] نصب و راه‌اندازی Celery  
- [ ] ایجاد Task ساده و بررسی عملکرد  
- [ ] اضافه کردن Celery Beat برای زمان‌بندی Taskها  

---

## 🔹 فاز 9 – Cache و Performance
- [ ] اتصال Django به Redis برای Cache  
- [ ] پیاده‌سازی cache_page و low-level cache  
- [ ] تست سرعت API بعد از فعال‌سازی Cache  

---

## 🔹 فاز 10 – Deploy و CI/CD
- [ ] تنظیم Gunicorn و Nginx در Docker  
- [ ] ساخت docker-compose-prod.yml  
- [ ] آماده‌سازی VPS (نصب Docker و اضافه کردن SSH-key)  
- [ ] تنظیم GitHub Actions برای CI و CD  
- [ ] استقرار پروژه روی VPS / Hamravesh / Dokploy  
- [ ] تست نهایی عملکرد پروژه در سرور  

---

## 🔹 فاز 11 – مانیتورینگ و نگهداری
- [ ] نصب و اتصال Sentry برای گزارش خطاها  
- [ ] ایجاد Backup خودکار از دیتابیس  
- [ ] اجرای Load Testing با Locust  
- [ ] مانیتورینگ performance سرور