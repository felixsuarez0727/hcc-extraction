from typing import TypedDict, Optional


class PatientState(TypedDict):
    patient_note: str
    extracted_patient_data: Optional[dict]
    extracted_medical_conditions: Optional[list]
    patient_information: Optional[dict]
    medical_assessments: Optional[list]
