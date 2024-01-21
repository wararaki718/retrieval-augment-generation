from functools import partial

import requests

from .builder import PromptBuilder


class RAGService:
    def __init__(self, retriever_api_url: str, generator_api_url: str) -> None:
        self._retrieve = partial(
            requests.post,
            headers={'Content-Type': 'application/json'},
            url=retriever_api_url,
            timeout=60
        )
        self._generate = partial(
            requests.post,
            headers={'Content-Type': 'application/json'},
            url=generator_api_url,
            timeout=60
        )

    def search(self, text: str) -> str:
        # retrieve
        response = self._retrieve(json={"content": text}).json()
        documents: list = response["texts"]

        # generate
        prompt = PromptBuilder.build(text, documents)
        response = self._generate(json={"text": prompt}).json()
        return response["text"]
