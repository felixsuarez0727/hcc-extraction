import os

from src.utils.db_helper import get_by_code


class MedicalAIEvaluator:
    def evaluate_hcc_relevance(self, medical_conditions):
        hcc_relevant = []
        hcc_not_relevant = []
        for condition in medical_conditions:
            clean_code = condition["code"].strip().replace(".", "").upper()
            hcc_condition = get_by_code(clean_code)

            if hcc_condition:
                hcc_relevant.append(condition)
            else:
                hcc_not_relevant.append(condition)

        return {"hcc_relevant": hcc_relevant, "hcc_not_relevant": hcc_not_relevant}
