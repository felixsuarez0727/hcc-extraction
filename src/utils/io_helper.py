import csv
from datetime import datetime

from src.utils.constants import OUTPUT_PATH


def read_csv(file_path):
    """Read a CSV file and return its contents as a set of unique tuples."""
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # Skip headers
        next(reader)
        return set(tuple(row) for row in reader)


def read_txt(file_path):
    """Read a txt file and return its content."""
    with open(file_path, newline="", encoding="utf-8") as textfile:
        return textfile.read()

def save_txt(state):
    """Save the extracted patient data and medical conditions to a text file."""
    
    patient_info = state["patient_information"]
    medical_conditions = state["medical_assessments"]
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    result = "Patient Information:\n"
    result += f"\tName: {patient_info['name']}\n"
    result += f"\tAge: {patient_info['age']}\n"
    result += f"\tDOB: {patient_info['dob']}\n"
    result += f"\tInsurance #: {patient_info['insurance_number']}\n\n"
    
    result += "Medical Conditions:\n"
    result += "\tHCC Relevant:\n"
    for condition in medical_conditions['hcc_relevant']:
        result += f"\t  - {condition['condition']} (Code: {condition['code']})\n"
    
    result += "\tHCC Not Relevant:\n"
    for condition in medical_conditions['hcc_not_relevant']:
        result += f"\t  - {condition['condition']} (Code: {condition['code']})\n"
    
    with open(f"{OUTPUT_PATH}/patient_result_{timestamp}.txt", "w") as file:
        file.write(result)