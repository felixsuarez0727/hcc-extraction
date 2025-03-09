import os

from app.src.utils.db_helper import get_by_code


class MedicalAIEvaluator:
    def __init__(self, service_account_path: str):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

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
