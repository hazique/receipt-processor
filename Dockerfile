# Base image to be reused
FROM python:3 as base
RUN apt-get update
WORKDIR /flask-app
COPY . /flask-app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Production image'
FROM base as prod
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:app"]