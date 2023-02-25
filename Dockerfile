FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]