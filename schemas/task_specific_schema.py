# schemas/task_specific_schema.py

from schemas.base_schema import BaseSchema


class TaskSpecificSchema(BaseSchema):
    def __init__(self, agents: dict):
        """
        agents: dict mapping task types to agent instances
        """
        self.agents = agents

    def run(self, task: str, context: dict = None) -> dict:
        start_time = time.time()
        total_tokens = 0
        results = []

        # Example of task allocation logic
        if "ethical" in task.lower():
            selected_agents = [self.agents['chain_of_thought'], self.agents['self_consistency']]
        elif "logical" in task.lower():
            selected_agents = [self.agents['backward_reasoning'], self.agents['commonsense_reasoning']]
        else:
            selected_agents = [self.agents['commonsense_reasoning']]

        for agent in selected_agents:
            result = agent.generate_response(task, context)
            results.append(result['response'])
            total_tokens += result['tokens_used']

        combined_result = "\n---\n".join(results)
        end_time = time.time()
        execution_time = end_time - start_time

        return {
            "schema": "Task-Specific",
            "result": combined_result,
            "tokens_used": total_tokens,
            "execution_time": execution_time
        }
