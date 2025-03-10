EXTRACTION_PROMPTS = {
    "patient_information_prompt": """
        You are a specialized medical AI assistant. Extract the information from the provided clinical note.
       
        Format your response as a JSON object with the following structure:
        "name": "Full name,
        "age": "Age",
        "dob": "Date of birth",
        "insurance_number": "Insurance number"

        Clinical Note:
        """,
    "medical_conditions_prompt": """
        You are a specialized medical AI assistant. Extract all medical conditions and their associated codes from the following clinical note.
        For each condition:
        1. Identify the condition name
        2. Extract any associated code (ICD-10)
    
        Format your response as a JSON with only an array called medical_conditions with objects having condition and code

        Assessment/Plan section:
        """,
}
