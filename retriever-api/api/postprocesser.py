from typing import List


class Postprocessor:
    def __init__(self) -> None:
        pass

    def transform(self, response: dict) -> List[str]:
        hits: dict = response["hits"]["hits"]
        texts = [hit["_source"]["text"] for hit in hits]
        return texts
