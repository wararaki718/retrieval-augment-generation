from typing import List


class PromptBuilder:
    @classmethod
    def build(cls, text: str, documents: List[str]) -> str:
        docs = "\n".join(documents)
        prompt = f"Answer the question '{text}'. If you do not have the answer, please refer to the below texts. \n{docs}"
        return prompt
