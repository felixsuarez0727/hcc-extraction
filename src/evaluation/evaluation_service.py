from typing import Any

from src.evaluation.evaluators import HCCRelevanceEvaluator

class EvaluationService:
    """Service to coordinate multiple evaluators."""
    
    def __init__(self):
        self.evaluators = {
            "hcc_relevance": HCCRelevanceEvaluator()
        }
    
    def evaluate(self, evaluator_name: str, data: Any) -> Any:
        """Evaluate data using the specified evaluator."""
        if evaluator_name not in self.evaluators:
            raise ValueError(f"Evaluator '{evaluator_name}' not found")
            
        evaluator = self.evaluators[evaluator_name]
        return evaluator.evaluate(data)
