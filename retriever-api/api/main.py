import os
from fastapi import FastAPI

from .schema.request import Text
from .schema.response import Answer
from .service import RetrieveService


app = FastAPI()
service = RetrieveService(
    host=os.getenv("OPENSEARCH_HOST", default="localhost"),
    port=int(os.getenv("OPENSEARCH_PORT", default="9200")),
    index_name=os.getenv("OPENSEARCH_INDEX", default="rag-index"),
)


@app.post("/retrieve", response_model=Answer)
def retrieve(request: Text) -> Answer:
    texts = service.retrieve(request)
    return Answer(texts=texts)
