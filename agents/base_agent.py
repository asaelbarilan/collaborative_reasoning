# agents/base_agent.py

from abc import ABC, abstractmethod
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class BaseAgent(ABC):
    def __init__(self, model_name="microsoft/DialoGPT-medium", device=None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    @abstractmethod
    def generate_response(self, task: str, context: dict = None) -> dict:
        pass

    def _generate(self, prompt: str, max_length: int = 150) -> dict:
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            early_stopping=True
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        tokens_used = outputs.shape[-1]
        return {"response": response.strip(), "tokens_used": tokens_used}
