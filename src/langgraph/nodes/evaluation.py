import logging
from src.evaluation.evaluation_service import EvaluationService
from src.langgraph.states.patient_state import PatientState
from src.utils.io_helper import save_txt

logger = logging.getLogger(__name__)


def evaluate_medical_conditions(state: PatientState) -> PatientState:
    """Evaluate the medical conditions of the patient."""

    logger.info("Starting evaluation of medical conditions.")

    try:
        evaluation_service = EvaluationService()

        logger.info("Evaluation instance created successfully.")

        evaluated_medical_conditions = evaluation_service.evaluate(
            "hcc_relevance", state["medical_assessments"]
        )

        logger.info("Medical conditions evaluated successfully.")

        state["medical_assessments"] = evaluated_medical_conditions
        logger.debug(f"Updated medical assessments: {state['medical_assessments']}")

    except Exception as e:
        logger.error(f"Error while evaluating medical conditions: {e}")
        raise

    return state


def save_patient_results(state: PatientState) -> PatientState:
    """Save the patient results to a text file."""

    logger.info("Starting to save patient results.")

    try:
        save_txt(state)
        logger.info("Patient results saved successfully.")

    except Exception as e:
        logger.error(f"Error while saving patient results: {e}")
        raise

    return state
