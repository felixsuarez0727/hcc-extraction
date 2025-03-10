import logging
from src.extraction.extractor import MedicalAIExtractor
from src.langgraph.states.patient_state import PatientState
from src.utils.constants import CREDENTIALS_FILE

logger = logging.getLogger(__name__)


def extract_patient_information(state: PatientState) -> PatientState:
    logger.info("Starting patient information extraction.")

    try:
        extractor = MedicalAIExtractor(service_account_path=CREDENTIALS_FILE)
        logger.info("MedicalAIExtractor instance created successfully.")

        state["patient_note"] = state["patient_note"].replace('"', "").replace("'", "")
        logger.debug(f"Patient note cleaned: {state['patient_note']}")

        state["extracted_patient_data"] = extractor.extract_patient_information(
            state["patient_note"]
        )
        logger.info("Patient data extracted successfully.")

        state["extracted_medical_conditions"] = extractor.extract_assessment_plan(
            state["patient_note"]
        )
        logger.info("Medical conditions (assessment plan) extracted successfully.")

    except Exception as e:
        logger.error(f"Error while extracting patient information: {e}")
        raise

    return state


def extract_medical_conditions(state: PatientState) -> PatientState:
    logger.info("Starting medical conditions extraction.")

    try:
        extractor = MedicalAIExtractor(service_account_path=CREDENTIALS_FILE)
        logger.info("MedicalAIExtractor instance created successfully.")

        state["patient_information"] = extractor.patient_data_ai_extraction(
            state["extracted_patient_data"]
        )
        logger.info("Patient information processed successfully.")

        state["medical_assessments"] = extractor.medical_conditions_ai_extraction(
            state["extracted_medical_conditions"]
        )
        logger.info("Medical assessments processed successfully.")

    except Exception as e:
        logger.error(f"Error while extracting medical conditions: {e}")
        raise

    return state
