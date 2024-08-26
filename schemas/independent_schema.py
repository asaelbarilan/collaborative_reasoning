# schemas/independent_schema.py

from schemas.base_schema import BaseSchema


class IndependentSchema(BaseSchema):
    def run(self, task: str, context: dict = None) -> dict:
        start_time = time.time()
        results = []
        total_tokens = 0

        for agent in self.agents:
            result = agent.generate_response(task, context)
            results.append(result['response'])
            total_tokens += result['tokens_used']

        end_time = time.time()
        execution_time = end_time - start_time

        combined_result = "\n---\n".join(results)

        return {
            "schema": "Independent",
            "result": combined_result,
            "tokens_used": total_tokens,
            "execution_time": execution_time
        }
