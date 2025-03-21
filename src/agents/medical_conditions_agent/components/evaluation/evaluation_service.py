from typing import Any

from src.agents.medical_conditions_agent.components.evaluation.evaluators import (
    HCCRelevanceEvaluator,
)


class EvaluationService:
    """Service to coordinate multiple evaluators."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.evaluators = {"hcc_relevance": HCCRelevanceEvaluator()}

    def evaluate(self, evaluator_name: str, data: Any) -> Any:
        """Evaluate data using the specified evaluator."""
        if evaluator_name not in self.evaluators:
            raise ValueError(f"Evaluator '{evaluator_name}' not found")

        evaluator = self.evaluators[evaluator_name]
        return evaluator.evaluate(data)
