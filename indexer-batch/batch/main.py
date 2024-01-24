import os
from pathlib import Path
from time import sleep

from opensearchpy import OpenSearch

from .builder import BulkDataBuilder
from .loader import IndexLoader, TextLoadInterator
from .vectorizer import DenseVectorizer


def batch() -> None:
    host = os.getenv("OPENSEARCH_HOST", default="localhost")
    port = int(os.getenv("OPENSEARCH_PORT", default="9200"))
    index_name = os.getenv("OPENSEARCH_INDEX", default="rag-index")

    client = OpenSearch(hosts=[{"host": host, "port": port}])
    index_body = IndexLoader.load(Path("./data/index.json"))

    response = client.indices.create(index_name, body=index_body)
    print(f"'{index_name}' index is created: {response}")
    print()
    sleep(1)

    model_name = "sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco"
    vectorizer = DenseVectorizer(model_name)

    bulk_data = []
    iterator = TextLoadInterator(Path("./data/data.txt"))
    for i, text in enumerate(iterator):
        vector = vectorizer.transform(text)
        data = BulkDataBuilder.build(index_name, i, text, vector)
        bulk_data.append(data)
    response = client.bulk("\n".join(bulk_data))
    print(f"data inserted: {response}")
    sleep(3)

    print("DONE")


if __name__ == "__main__":
    batch()
