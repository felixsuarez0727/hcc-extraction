import pytest
from src.agents.medical_conditions_agent.states.patient_state import PatientState

@pytest.fixture
def valid_patient_state():
    ''' Return a PatientState object with valid fields. '''
    return PatientState(
        patient_note="Sample patient note.",
        patient_information={"name": "John Doe", "age": 30},
        medical_conditions=[{"condition": "Diabetes", "code": "E11.9"}]
    )

@pytest.fixture
def invalid_patient_state():
    ''' Return a PatientState object with invalid fields. '''
    return PatientState(
        patient_note="Sample patient note.",
        patient_information=None,
        medical_conditions=None
    )

def test_patient_state_valid(valid_patient_state):
    ''' Test that valid fields are set correctly. '''
    assert isinstance(valid_patient_state["patient_note"], str)
    assert isinstance(valid_patient_state["patient_information"], dict)
    assert isinstance(valid_patient_state["medical_conditions"], list)

    assert valid_patient_state["patient_note"] == "Sample patient note."
    assert valid_patient_state["patient_information"]["name"] == "John Doe"
    assert valid_patient_state["medical_conditions"][0]["condition"] == "Diabetes"

def test_patient_state_invalid(invalid_patient_state):
    ''' Test that invalid fields are set to None when not provided. '''
    assert isinstance(invalid_patient_state["patient_note"], str)
    assert invalid_patient_state["patient_information"] is None
    assert invalid_patient_state["medical_conditions"] is None

def test_patient_state_optional_fields():
    ''' Test that optional fields are set to None when not provided. '''
    state_with_empty_data = PatientState(
        patient_note="Patient note only.",
        patient_information=None,
        medical_conditions=None
    )

    assert state_with_empty_data["patient_information"] is None
    assert state_with_empty_data["medical_conditions"] is None

