import os

from app.src.utils.constants import (
    BASE_DIR,
    DATABASE_FILE,
    HCC_FILE,
    CREDENTIALS_FILE,
    INPUT_PATH,
    OUTPUT_PATH,
    PROMPTS,
)


def test_base_dir():
    """Test that the BASE_DIR constant is set correctly."""
    assert BASE_DIR == "app", f"Expected 'app', but got {BASE_DIR}"


def test_database_file():
    """Test that the DATABASE_FILE constant is set correctly."""
    expected_path = os.path.join("app", "data", "reference", "hcc_relevant_codes.db")
    assert DATABASE_FILE == expected_path, (
        f"Expected {expected_path}, but got {DATABASE_FILE}"
    )


def test_hcc_file():
    """Test that the HCC_FILE constant is set correctly."""
    expected_path = os.path.join("app", "data", "reference", "hcc_relevant_codes.csv")
    assert HCC_FILE == expected_path, f"Expected {expected_path}, but got {HCC_FILE}"


def test_credentials_file():
    """Test that the CREDENTIALS_FILE constant is set correctly."""
    expected_path = os.path.join("app", "credentials.json")
    assert CREDENTIALS_FILE == expected_path, (
        f"Expected {expected_path}, but got {CREDENTIALS_FILE}"
    )


def test_input_path():
    """Test that the INPUT_PATH constant is set correctly."""
    expected_path = os.path.join("app", "data", "input")
    assert INPUT_PATH == expected_path, (
        f"Expected {expected_path}, but got {INPUT_PATH}"
    )


def test_output_path():
    """Test that the OUTPUT_PATH constant is set correctly."""
    expected_path = os.path.join("app", "data", "output")
    assert OUTPUT_PATH == expected_path, (
        f"Expected {expected_path}, but got {OUTPUT_PATH}"
    )


def test_prompts_keys():
    """Test that the PROMPTS dictionary has the correct keys."""
    assert "patient_information_prompt" in PROMPTS
    assert "medical_conditions_prompt" in PROMPTS


def test_prompts_values():
    """Test that the prompts are strings and have content."""
    assert isinstance(PROMPTS["patient_information_prompt"], str)
    assert isinstance(PROMPTS["medical_conditions_prompt"], str)
    assert len(PROMPTS["patient_information_prompt"]) > 0
    assert len(PROMPTS["medical_conditions_prompt"]) > 0
