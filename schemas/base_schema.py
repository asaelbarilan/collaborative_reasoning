# schemas/base_schema.py

from abc import ABC, abstractmethod
from typing import List, Dict
import time


class BaseSchema(ABC):
    def __init__(self, agents: List):
        self.agents = agents

    @abstractmethod
    def run(self, task: str, context: dict = None) -> dict:
        pass
