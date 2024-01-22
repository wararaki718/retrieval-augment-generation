FROM python:3.10

WORKDIR /opt/app
COPY ./generator-api /opt/app
RUN pip install poetry

RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0" ]
