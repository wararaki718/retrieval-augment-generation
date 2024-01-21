from pydantic import BaseModel


class RAGQuestion(BaseModel):
    text: str
