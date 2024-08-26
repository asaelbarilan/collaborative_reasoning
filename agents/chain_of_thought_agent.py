# agents/chain_of_thought_agent.py

from agents.base_agent import BaseAgent

class ChainOfThoughtAgent(BaseAgent):
    def generate_response(self, task: str, context: dict = None) -> dict:
        prompt = f"Let's think step by step to solve the following problem:\n\nTask: {task}\n\nAnswer:"
        return self._generate(prompt)
