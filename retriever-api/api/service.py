from functools import partial
from typing import List

from opensearchpy import OpenSearch

from .builder import QueryBuilder
from .postprocesser import Postprocessor
from .schema.request import Text
from .vectorizer import DenseVectorizer


class RetrieveService:
    def __init__(self, host: str="localhost", port: int=9200) -> None:
        model_name = "sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco"
        self._vectorizer = DenseVectorizer(model_name)

        index_name = "rag-index"
        client = OpenSearch(hosts=[{"host": host, "port": port}])
        self._search = partial(client.search, index=index_name)

        self._postprocessor = Postprocessor()

    def retrieve(self, text: Text) -> List[str]:
        vector = self._vectorizer.transform(text.content)
        query = QueryBuilder.build(vector)
        response = self._search(query)
        texts = self._postprocessor.transform(response)

        return texts
