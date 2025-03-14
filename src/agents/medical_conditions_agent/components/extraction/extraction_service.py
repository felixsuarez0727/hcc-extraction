from typing import Any

from src.agents.medical_conditions_agent.components.extraction.extractors import (
    RegexExtractor,
    AIPatientInformationExtractor,
    AIMedicalConditionsExtractor,
)


class ExtractionService:
    """Service to coordinate multiple extractors."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.extractors = {
            "patient_info": RegexExtractor(
                pattern=r"(?i)^(.*?)\s*Chief Complaint",
                section_name="patient_information",
            ),
            "assessment_plan": RegexExtractor(
                pattern=r"(?i)assessment\s*/?\s*plan:?\s*(.*)",
                section_name="assessment_plan",
            ),
            "patient_data": AIPatientInformationExtractor(
                prompt_key="patient_information_prompt"
            ),
            "medical_conditions": AIMedicalConditionsExtractor(
                prompt_key="medical_conditions_prompt"
            ),
        }

    def extract(self, extractor_name: str, clinical_note: str) -> Any:
        """Extract information using the specified extractor."""
        if extractor_name not in self.extractors:
            raise ValueError(f"Extractor '{extractor_name}' not found")

        extractor = self.extractors[extractor_name]
        return extractor.extract(clinical_note)
