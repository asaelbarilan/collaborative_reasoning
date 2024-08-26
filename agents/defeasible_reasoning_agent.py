# agents/defeasible_reasoning_agent.py

from agents.base_agent import BaseAgent

class DefeasibleReasoningAgent(BaseAgent):
    def generate_response(self, task: str, context: dict = None) -> dict:
        premises = context.get('premises', '')
        new_information = context.get('new_information', '')
        prompt = (f"Given the premises:\n{premises}\n\n"
                  f"Considering the new information:\n{new_information}\n\n"
                  f"How should our conclusion about '{task}' be updated?")
        return self._generate(prompt)
