from fastapi import FastAPI

from .schema.request import Text
from .schema.response import Answer
from .service import RetrieveService


app = FastAPI()
service = RetrieveService(host="opensearch")


@app.post("/retrieve", response_model=Answer)
def retrieve(request: Text) -> Answer:
    texts = service.retrieve(request)
    return Answer(texts=texts)
