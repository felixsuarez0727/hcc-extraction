from langgraph.graph import StateGraph, START, END

from src.utils.constants import HCC_FILE
from src.utils.io_helper import read_csv
from src.utils.db_helper import create_database, insert_data
from src.utils.logging_config import setup_logging


from src.agents.medical_conditions_agent.states.patient_state import PatientState

from src.agents.medical_conditions_agent.nodes.evaluation import (
    evaluate_medical_conditions,
    save_patient_results,
)


from src.agents.medical_conditions_agent.nodes.extraction import (
    extract_medical_conditions,
    extract_patient_information,
)


def init_database():
    create_database()
    hcc_data = read_csv(HCC_FILE)
    insert_data(hcc_data)


# Initialize HCC database
init_database()
setup_logging()


# Define the state graph
graph = StateGraph(PatientState)

# Define nodes
graph.add_node("extract_patient_information", extract_patient_information)
graph.add_node("extract_medical_conditions", extract_medical_conditions)
graph.add_node("evaluate_medical_conditions", evaluate_medical_conditions)
graph.add_node("save_patient_results", save_patient_results)

# Define edges
graph.add_edge(START, "extract_patient_information")
graph.add_edge("extract_patient_information", "extract_medical_conditions")
graph.add_edge("extract_medical_conditions", "evaluate_medical_conditions")
graph.add_edge("evaluate_medical_conditions", "save_patient_results")
graph.add_edge("save_patient_results", END)

graph = graph.compile()
