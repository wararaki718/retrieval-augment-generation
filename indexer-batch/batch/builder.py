import json
from typing import List


class BulkDataBuilder:
    @classmethod
    def build(cls, index_name: str, id_: int, text: str, vector: List[float]) -> str:
        index = json.dumps({
            "index": {
                "_index": index_name,
                "_id": id_,
            },
        })
        data = json.dumps({
            "rag_vector": vector,
            "text": text,
        })
        return f"{index}\n{data}"
