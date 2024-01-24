import os

from fastapi import FastAPI

from .schema.request import RAGQuestion
from .schema.response import RAGAnswer
from .service import RAGService


app = FastAPI()
service = RAGService(
    os.getenv("RETRIEVER_URL", default="http://retriever-api:4000/retrieve"),
    os.getenv("GENERATOR_URL", default="http://generator-api:8000/generate"),
)

@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/search", response_model=RAGAnswer)
def search(question: RAGQuestion) -> RAGAnswer:
    text = service.search(question.text)
    return RAGAnswer(text=text)
