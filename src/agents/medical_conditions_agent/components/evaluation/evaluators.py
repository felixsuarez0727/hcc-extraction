import logging
from typing import Dict, List, Any

from src.utils.db_helper import get_by_code

logger = logging.getLogger(__name__)

class BaseEvaluator:
    """Base class for all evaluators."""
    def evaluate(self, medical_conditions):
        """Evaluate the given data."""
        raise NotImplementedError("Subclasses must implement this method")


class HCCRelevanceEvaluator(BaseEvaluator):
    """Evaluator to determine HCC relevance of medical conditions."""
    
    def evaluate(self, medical_conditions: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Evaluate medical conditions for HCC relevance.
        """
        logger.info("Evaluating HCC relevance for medical conditions")
        hcc_relevant = []
        hcc_not_relevant = []
        
        for condition in medical_conditions:
            clean_code = condition["code"].strip().replace(".", "").upper()
            hcc_condition = get_by_code(clean_code)

            if hcc_condition:
                logger.debug(f"Condition with code {clean_code} is HCC relevant")
                hcc_relevant.append(condition)
            else:
                logger.debug(f"Condition with code {clean_code} is not HCC relevant")
                hcc_not_relevant.append(condition)

        result = {
            "hcc_relevant": hcc_relevant, 
            "hcc_not_relevant": hcc_not_relevant
        }
        
        logger.info(f"HCC evaluation complete. Found {len(hcc_relevant)} relevant conditions")
        return result
