# translator.py

from llama_cpp import Llama
from config import LLAMA_MODEL_PATH

class Translator:
    def __init__(self):
        self.llm = Llama(model_path=LLAMA_MODEL_PATH, n_ctx=2048)

    def translate(self, text):
        prompt = f"Translate English to Hindi:\n{text}\nHindi:"
        output = self.llm(prompt, max_tokens=128)
        return output["choices"][0]["text"].strip()
