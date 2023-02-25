FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./api /api
COPY ./requirements.txt /opt/requirements.txt

RUN pip install -U pip && \
    pip install -r /opt/requirements.txt && \
    rm /opt/requirements.txt && \
    pip cache purge

WORKDIR /
CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["gunicorn", "api.main:app", "--worker-class"]