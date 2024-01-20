# generator api

## setup

```shell
poetry install
```

## run

```shell
poetry run uvicorn api.main:app
```

open http://localhost:8000/docs on your browser.

sample question

```json
{
  "content": "Where is the capital of Japan?"
}
```
