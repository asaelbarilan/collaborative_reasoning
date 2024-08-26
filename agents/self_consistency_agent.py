# agents/self_consistency_agent.py

from agents.base_agent import BaseAgent

class SelfConsistencyAgent(BaseAgent):
    def generate_response(self, task: str, context: dict = None) -> dict:
        prompt = f"Consider multiple perspectives and provide the most consistent answer to the following question:\n\nQuestion: {task}\n\nAnswer:"
        return self._generate(prompt)
