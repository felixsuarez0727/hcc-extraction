import json
import logging
import time
import re
import os

from src.langgraph.prompts.extraction_prompts import EXTRACTION_PROMPTS
from vertexai.generative_models import GenerativeModel

logger = logging.getLogger(__name__)

class MedicalAIExtractor:
    def __init__(self, service_account_path: str):
        logger.info("Initializing MedicalAIExtractor.")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path
        self.model = GenerativeModel(model_name="gemini-1.5-flash")
        logger.info("MedicalAIExtractor initialized successfully.")

    def _extract_section(self, pattern, clinical_note):
        """Extract the section from the clinical note using the given pattern."""
        logger.debug(f"Extracting section with pattern: {pattern}")
        match = re.search(pattern, clinical_note, re.DOTALL)
        if match:
            extracted_text = str(match.group(1).strip())
            logger.debug(f"Section extracted successfully: {extracted_text}")
            return extracted_text
        logger.warning("No match found for the given pattern.")
        return clinical_note

    def extract_patient_information(self, clinical_note: str) -> str:
        """Extract the patient information from the clinical note."""
        logger.info("Extracting patient information.")
        pattern = r"(?i)^(.*?)\s*Chief Complaint"
        return self._extract_section(pattern, clinical_note)

    def extract_assessment_plan(self, clinical_note: str) -> str:
        """Extract the assessment/plan section from the clinical note."""
        logger.info("Extracting assessment/plan information.")
        pattern = r"(?i)assessment\s*/?\s*plan:?\s*(.*)"
        return self._extract_section(pattern, clinical_note)

    def patient_data_ai_extraction(self, clinical_note: str) -> dict:
        """Extract patient data from the clinical note using AI."""
        logger.info("Starting AI extraction for patient data.")
        time.sleep(0.3)
        prompt = f"{EXTRACTION_PROMPTS.get('patient_information_prompt')} {clinical_note}"
        logger.debug("Generated prompt for patient data extraction...")  
        response = self.model.generate_content(prompt)
        text_patient_information = response.text.strip()
        logger.info("Patient data AI extraction completed.")
        try:
            return json.loads(text_patient_information)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON response: {e}")
            raise

    def medical_conditions_ai_extraction(self, clinical_note: str) -> list:
        """Extract medical conditions from the clinical note using AI."""
        logger.info("Starting AI extraction for medical conditions.")
        time.sleep(0.3)
        prompt = f"{EXTRACTION_PROMPTS.get('medical_conditions_prompt')} {clinical_note}"
        logger.debug("Generated prompt for medical conditions extraction...")  
        response = self.model.generate_content(prompt)
        conditions_text = response.text.strip()
        logger.info("Medical conditions AI extraction completed.")
        try:
            return json.loads(conditions_text)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON response: {e}")
            raise