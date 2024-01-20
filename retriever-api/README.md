# retriever api

## setup

```shell
poetry install
```

## run

```shell
poetry run uvicorn api.main:app --port 7000
```

open http://localhost:7000/docs on your browser.

sample question

```json
{
  "text": "Where is the capital of Japan?"
}
```
