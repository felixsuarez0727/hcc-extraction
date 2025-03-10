import os

from src.utils.constants import (
    BASE_DIR,
    DATABASE_FILE,
    HCC_FILE,
    CREDENTIALS_FILE,
    INPUT_PATH,
    OUTPUT_PATH,
)


def test_base_dir():
    """Test that the BASE_DIR constant is set correctly."""
    assert BASE_DIR == "", f"Expected '', but got {BASE_DIR}"


def test_database_file():
    """Test that the DATABASE_FILE constant is set correctly."""
    expected_path = os.path.join("", "data", "reference", "hcc_relevant_codes.db")
    assert DATABASE_FILE == expected_path, (
        f"Expected {expected_path}, but got {DATABASE_FILE}"
    )


def test_hcc_file():
    """Test that the HCC_FILE constant is set correctly."""
    expected_path = os.path.join("", "data", "reference", "hcc_relevant_codes.csv")
    assert HCC_FILE == expected_path, f"Expected {expected_path}, but got {HCC_FILE}"


def test_credentials_file():
    """Test that the CREDENTIALS_FILE constant is set correctly."""
    expected_path = os.path.join("", "credentials.json")
    assert CREDENTIALS_FILE == expected_path, (
        f"Expected {expected_path}, but got {CREDENTIALS_FILE}"
    )


def test_input_path():
    """Test that the INPUT_PATH constant is set correctly."""
    expected_path = os.path.join("", "data", "input")
    assert INPUT_PATH == expected_path, (
        f"Expected {expected_path}, but got {INPUT_PATH}"
    )


def test_output_path():
    """Test that the OUTPUT_PATH constant is set correctly."""
    expected_path = os.path.join("", "data", "output")
    assert OUTPUT_PATH == expected_path, (
        f"Expected {expected_path}, but got {OUTPUT_PATH}"
    )
