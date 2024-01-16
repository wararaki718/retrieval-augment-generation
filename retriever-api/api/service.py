from .schema.request import Text
from .vectorizer import DenseVectorizer


class RetrieveService:
    def __init__(self) -> None:
        model_name = "sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco"
        self._vectorizer = DenseVectorizer(model_name)

    def retrieve(self, text: Text) -> list:
        values = self._vectorizer.transform(text.content)
        # search
        return values
