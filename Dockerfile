FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./api /api
WORKDIR /
CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["gunicorn", "api.main:app", "--worker-class"]