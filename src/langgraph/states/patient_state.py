from typing import TypedDict, Optional


class PatientState(TypedDict):
    patient_note: str
    patient_information: Optional[dict]
    medical_conditions: Optional[list]
