import time
import os

from src.langgraph.states.patient_state import PatientState
from src.utils.constants import INPUT_PATH
from src.utils.io_helper import read_txt
from src.agent import graph


def main():
    input_path = INPUT_PATH

    patient_files = [f for f in os.listdir(input_path) if f.startswith("pn_")]

    for patient_file in patient_files:
        patient_note = read_txt(os.path.join(input_path, patient_file))

        initial_state = PatientState(
            patient_note=patient_note,
            patient_information={},
            medical_conditions=[],
        )

        graph.invoke(initial_state)

        time.sleep(60)


if __name__ == "__main__":
    main()
