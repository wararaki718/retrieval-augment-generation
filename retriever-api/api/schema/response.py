from typing import List

from pydantic import BaseModel


class Answer(BaseModel):
    texts: List[str]
