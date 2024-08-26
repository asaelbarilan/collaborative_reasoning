# schemas/competitive_schema.py

from schemas.base_schema import BaseSchema


class CompetitiveSchema(BaseSchema):
    def __init__(self, agents: List, evaluator):
        super().__init__(agents)
        self.evaluator = evaluator  # Function to evaluate and score responses

    def run(self, task: str, context: dict = None) -> dict:
        start_time = time.time()
        total_tokens = 0
        results = []

        for agent in self.agents:
            result = agent.generate_response(task, context)
            score = self.evaluator(result['response'])
            results.append({
                'response': result['response'],
                'score': score,
                'tokens_used': result['tokens_used']
            })
            total_tokens += result['tokens_used']

        # Select the best response based on score
        best_result = max(results, key=lambda x: x['score'])
        end_time = time.time()
        execution_time = end_time - start_time

        return {
            "schema": "Competitive",
            "result": best_result['response'],
            "score": best_result['score'],
            "tokens_used": total_tokens,
            "execution_time": execution_time
        }
