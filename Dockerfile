# # FROM python:3.13-slim
# # WORKDIR /app
# # COPY requirements.txt /app/
# # RUN pip install --upgrade pip && pip install -r requirements.txt
# # COPY . /app/
# # RUN python manage.py collectstatic --noinput
# # RUN python manage.py migrate
# # EXPOSE 8000

# # CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]

# FROM python:3.13-slim

# WORKDIR /app

# COPY requirements.txt /app/
# RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
# RUN pip install --upgrade pip && pip install -r requirements.txt

# COPY . /app/

# EXPOSE 8000

# # entrypoint می‌تونه همونجا migrate و collectstatic بزنه
# CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]



FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["gunicorn", "djangoProject.wsgi:application", "--bind", "0.0.0.0:8000"]