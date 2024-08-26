# agents/commonsense_reasoning_agent.py

from agents.base_agent import BaseAgent

class CommonsenseReasoningAgent(BaseAgent):
    def generate_response(self, task: str, context: dict = None) -> dict:
        prompt = f"Using commonsense reasoning, what is the most plausible answer to the following question?\n\nQuestion: {task}\n\nAnswer:"
        return self._generate(prompt)
