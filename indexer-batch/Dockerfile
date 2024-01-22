FROM python:3.10

WORKDIR /opt/app
COPY ./indexer-batch /opt/app
RUN pip install poetry

RUN poetry install

ENTRYPOINT [ "poetry", "run", "batch-index-runner" ]
