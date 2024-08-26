# schemas/sequential_schema.py

from schemas.base_schema import BaseSchema


class SequentialSchema(BaseSchema):
    def run(self, task: str, context: dict = None) -> dict:
        start_time = time.time()
        current_context = context or {}
        input_task = task
        total_tokens = 0

        for agent in self.agents:
            result = agent.generate_response(input_task, current_context)
            current_context['previous_response'] = result['response']
            input_task = result['response']
            total_tokens += result['tokens_used']

        end_time = time.time()
        execution_time = end_time - start_time

        final_result = current_context.get('previous_response', '')

        return {
            "schema": "Sequential",
            "result": final_result,
            "tokens_used": total_tokens,
            "execution_time": execution_time
        }
