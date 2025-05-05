# Явно указываем ARM64
FROM --platform=linux/arm64 python:3.11-slim-bookworm

WORKDIR /app

ENV PYTHONPATH=/app

RUN python -m pip install --upgrade pip

# RUN pip install celery==5.5.2
RUN pip install celery
