FROM python:3.10

WORKDIR /opt/app
COPY ./retriever-api /opt/app
RUN pip install poetry

RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "4000" ]
