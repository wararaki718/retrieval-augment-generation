from pydantic import BaseModel


class RAGAnswer(BaseModel):
    text: str
