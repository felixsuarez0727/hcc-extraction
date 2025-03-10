import json
import logging
import time
import re
from typing import Any

from vertexai.generative_models import GenerativeModel
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


class AIExtractor(BaseExtractor):
    """Base class for AI-powered extractors."""

    def __init__(self, prompt_key: str, output_type: str = "json"):
        self.model = GenerativeModel(model_name="gemini-1.5-flash")
        self.prompt_key = prompt_key
        self.output_type = output_type

    def extract(self, clinical_note: str) -> Any:
        """Extract information using AI."""
        logger.info(f"Starting AI extraction for {self.prompt_key}")
        time.sleep(0.3)

        prompt = f"{EXTRACTION_PROMPTS.get(self.prompt_key)} {clinical_note}"
        response = self.model.generate_content(prompt)
        text_response = response.text.strip()

        if self.output_type == "json":
            try:
                return json.loads(text_response)
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON response: {e}")
                raise
        return text_response
