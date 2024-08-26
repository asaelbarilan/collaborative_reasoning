# experiment_manager.py

from agents.chain_of_thought_agent import ChainOfThoughtAgent
from agents.backward_reasoning_agent import BackwardReasoningAgent
from agents.self_consistency_agent import SelfConsistencyAgent
from agents.defeasible_reasoning_agent import DefeasibleReasoningAgent
from agents.commonsense_reasoning_agent import CommonsenseReasoningAgent

from schemas.independent_schema import IndependentSchema
from schemas.sequential_schema import SequentialSchema
from schemas.task_specific_schema import TaskSpecificSchema
from schemas.competitive_schema import CompetitiveSchema

from evaluator import simple_evaluator


class ExperimentManager:
    def __init__(self):
        # Initialize agents
        self.chain_of_thought_agent = ChainOfThoughtAgent()
        self.backward_reasoning_agent = BackwardReasoningAgent()
        self.self_consistency_agent = SelfConsistencyAgent()
        self.defeasible_reasoning_agent = DefeasibleReasoningAgent()
        self.commonsense_reasoning_agent = CommonsenseReasoningAgent()

        # Initialize schemas
        self.schemas = [
            IndependentSchema([
                self.chain_of_thought_agent,
                self.backward_reasoning_agent,
                self.self_consistency_agent,
                self.defeasible_reasoning_agent,
                self.commonsense_reasoning_agent
            ]),
            SequentialSchema([
                self.chain_of_thought_agent,
                self.self_consistency_agent,
                self.commonsense_reasoning_agent
            ]),
            TaskSpecificSchema({
                'chain_of_thought': self.chain_of_thought_agent,
                'backward_reasoning': self.backward_reasoning_agent,
                'self_consistency': self.self_consistency_agent,
                'defeasible_reasoning': self.defeasible_reasoning_agent,
                'commonsense_reasoning': self.commonsense_reasoning_agent
            }),
            CompetitiveSchema([
                self.chain_of_thought_agent,
                self.backward_reasoning_agent,
                self.self_consistency_agent,
                self.defeasible_reasoning_agent,
                self.commonsense_reasoning_agent
            ], evaluator=simple_evaluator)
        ]

    def run_experiments(self, task: str, context: dict = None):
        results = []
        for schema in self.schemas:
            result = schema.run(task, context)
            results.append(result)
        return results
