import os

BASE_DIR = os.environ.get("APP_BASE_DIR", "app")

# File paths
DATABASE_FILE = os.path.join(BASE_DIR, "data", "reference", "hcc_relevant_codes.db")
HCC_FILE = os.path.join(BASE_DIR, "data", "reference", "hcc_relevant_codes.csv")
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")

# Data paths
INPUT_PATH = os.path.join(BASE_DIR, "data", "input")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")

PROMPTS = {
    "patient_information_prompt": """
        You are a specialized medical AI assistant. Extract the information from the provided clinical note.
       
        Format your response as a JSON object with the following structure:
        "name": "Full name,
        "age": "Age",
        "dob": "Date of birth",
        "insurance_number": "Insurance number"
        Do not add additional markdown information.

        Clinical Note:

        """,
    "medical_conditions_prompt": """
        You are a specialized medical AI assistant. Extract all medical conditions and their associated codes from the following clinical note.
        For each condition:
        1. Identify the condition name
        2. Extract any associated code (ICD-10)
    
        Format your response as a JSON array with objects having the following structure:
        [
            {
                "condition": "condition name",
                "code": "associated code (if available)",
            }
        ]
        Do not add additional markdown information.

         Assessment/Plan section:
        """,
}
