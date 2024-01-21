from fastapi import FastAPI

from .schema.request import RAGQuestion
from .schema.response import RAGAnswer
from .service import RAGService

app = FastAPI()
service = RAGService(
    "http://localhost:7000/retrieve",
    "http://localhost:8000/generate",
)

@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/search", response_model=RAGAnswer)
def search(question: RAGQuestion) -> RAGAnswer:
    text = service.search(question.text)
    return RAGAnswer(text=text)
