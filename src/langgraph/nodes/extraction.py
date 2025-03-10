import logging
from src.extraction.extraction_service import ExtractionService
from src.langgraph.states.patient_state import PatientState

logger = logging.getLogger(__name__)


def extract_patient_information(state: PatientState) -> PatientState:
    logger.info("Starting patient information extraction.")

    try:
        extraction_service = ExtractionService()
        logger.info("Extraction instance created successfully.")

        state["patient_note"] = state["patient_note"].replace('"', "").replace("'", "")
        logger.debug("Patient note cleaned.")

        extracted_patient_information = extraction_service.extract(
            "patient_info", state["patient_note"]
        )
        logger.info("Patient data extracted successfully.")

        state["patient_information"] = extraction_service.extract(
            "patient_data", extracted_patient_information
        )
        logger.info("Patient information processed successfully.")
        

    except Exception as e:
        logger.error(f"Error while extracting patient information: {e}")
        raise

    return state


def extract_medical_conditions(state: PatientState) -> PatientState:
    logger.info("Starting medical conditions extraction.")

    try:
        extraction_service = ExtractionService()
        logger.info("Extraction instance created successfully.")

        extracted_medical_conditions = extraction_service.extract(
            "assessment_plan", state["patient_note"]
        )
        logger.info("Medical conditions (assessment plan) extracted successfully.")

        state["medical_conditions"] = extraction_service.extract(
            "medical_conditions", extracted_medical_conditions
        )
        logger.info("Medical assessments processed successfully.")

    except Exception as e:
        logger.error(f"Error while extracting medical conditions: {e}")
        raise

    return state
