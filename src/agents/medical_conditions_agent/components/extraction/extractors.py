import logging
import time
import re
from typing import Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from src.agents.medical_conditions_agent.prompts.extraction_prompts import (
    EXTRACTION_PROMPTS,
)

logger = logging.getLogger(__name__)


class BaseExtractor:
    """Base class for all extractors."""

    def extract(self, clinical_note: str) -> Any:
        """Extract information from clinical note."""
        raise NotImplementedError("Subclasses must implement this method")


class RegexExtractor(BaseExtractor):
    """Extract sections using regex patterns."""

    def __init__(self, pattern: str, section_name: str):
        self.pattern = pattern
        self.section_name = section_name

    def extract(self, clinical_note: str) -> str:
        """Extract section using regex pattern."""
        logger.debug(f"Extracting {self.section_name} with pattern")
        match = re.search(self.pattern, clinical_note, re.DOTALL)
        if match:
            extracted_text = str(match.group(1).strip())
            logger.debug(f"{self.section_name} extracted successfully")
            return extracted_text
        logger.warning(f"No match found for {self.section_name}")
        return clinical_note


class AIPatientInformationExtractor(BaseExtractor):
    """AI-based extractor to obtain Patient Information"""

    def __init__(self, prompt_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        self.prompt_key = prompt_key

        self.output_parser = StructuredOutputParser.from_response_schemas([
            ResponseSchema(name="name", description="Patient's name"),
            ResponseSchema(name="age", description="Patient's age"),
            ResponseSchema(name="dob", description="Patient's date of birth"),
            ResponseSchema(name="insurance_number", description="Patient's insurance number")
        ])

    def extract(self, clinical_note: str) -> any:
        """Extract information using AI with a structured prompt"""
        logger.info(f"Starting AI extraction for {self.prompt_key}")
        time.sleep(0.3)

        prompt = PromptTemplate(
            input_variables=["clinical_note"],
            template=f"{EXTRACTION_PROMPTS.get("patient_information_prompt")} {{clinical_note}}"
        ).format(clinical_note=clinical_note)

        response = self.llm.predict(prompt)
        result = self.output_parser.parse(response)
        try:
            return result
        except Exception as e:
            logger.error(f"Error parsing output: {e}")
            raise



class AIMedicalConditionsExtractor(BaseExtractor):
    """AI-based extractor to obtain Medical Conditions"""

    def __init__(self, prompt_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        self.prompt_key = prompt_key

        self.output_parser = StructuredOutputParser.from_response_schemas([
            ResponseSchema(name="medical_conditions", description="List of medical conditions and codes", type="array", items=[
                ResponseSchema(name="condition", description="Medical condition description", type="string"),
                ResponseSchema(name="code", description="Medical condition code", type="string")
            ])
        ])

    def extract(self, clinical_note: str) -> any:
        """Extract information using AI with a structured prompt"""
        logger.info(f"Starting AI extraction for {self.prompt_key}")
        time.sleep(0.3)

        prompt = PromptTemplate(
            input_variables=["clinical_note"],
            template=f"{EXTRACTION_PROMPTS.get('medical_conditions_prompt')} {{clinical_note}}"
        ).format(clinical_note=clinical_note)

        response = self.llm.predict(prompt)
        result = self.output_parser.parse(response)

        try:
            return result.get("medical_conditions", "")
        except Exception as e:
            logger.error(f"Error parsing output: {e}")
            raise