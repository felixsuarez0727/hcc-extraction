import time
import os

from app.src.langgraph.states.patient_state import PatientState
from app.src.utils.constants import INPUT_PATH
from app.src.utils.io_helper import read_txt
from app.agent import graph


def main():
    input_path = INPUT_PATH

    patient_files = [f for f in os.listdir(input_path) if f.startswith("pn_")]

    for patient_file in patient_files:
        patient_note = read_txt(os.path.join(input_path, patient_file))

        initial_state = PatientState(
            patient_note=patient_note,
            extracted_patient_data="",
            extracted_medical_conditions="",
            patient_information={},
            medical_assessments=[],
        )

        graph.invoke(initial_state)

        time.sleep(60)


if __name__ == "__main__":
    main()
