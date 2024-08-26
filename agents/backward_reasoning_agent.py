# agents/backward_reasoning_agent.py

from agents.base_agent import BaseAgent

class BackwardReasoningAgent(BaseAgent):
    def generate_response(self, task: str, context: dict = None) -> dict:
        prompt = f"Given the conclusion: '{task}', let's work backwards to identify the premises and reasoning that lead to it."
        return self._generate(prompt)
