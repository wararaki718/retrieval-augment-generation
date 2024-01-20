from typing import List


class QueryBuilder:
    @classmethod
    def build(cls, vector: List[float], k: int=2, size: int=2) -> dict:
        query: dict = {
            "size": size,
            "query": {
                "knn": {
                    "rag-index": {
                        "vector": vector,
                        "k": k,
                    }
                }
            }
        }
        return query
