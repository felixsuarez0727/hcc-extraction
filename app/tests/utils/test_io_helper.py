import pytest
from unittest import mock


from app.src.utils.io_helper import read_csv, read_txt, save_txt

OUTPUT_PATH = "/mock/output"


@pytest.fixture
def sample_csv_data():
    return "header1,header2\nvalue1,value2\nvalue3,value4\n"


@pytest.fixture
def sample_txt_data():
    return "This is a sample text file."


@pytest.fixture
def mock_state():
    return {
        "patient_information": {
            "name": "John Doe",
            "age": "30",
            "dob": "1995-01-01",
            "insurance_number": "123456789",
        },
        "medical_assessments": {
            "hcc_relevant": [{"condition": "Diabetes", "code": "E11.9"}],
            "hcc_not_relevant": [{"condition": "Asthma", "code": "J45"}],
        },
    }


def test_read_csv(sample_csv_data):
    """Test that the read_csv function reads the correct content from a file."""
    with mock.patch("builtins.open", mock.mock_open(read_data=sample_csv_data)):
        result = read_csv("mock_path.csv")
        expected = {("value1", "value2"), ("value3", "value4")}
        assert result == expected, f"Expected {expected}, but got {result}"


def test_read_txt(sample_txt_data):
    """Test that the read_txt function reads the correct content from a file."""
    with mock.patch("builtins.open", mock.mock_open(read_data=sample_txt_data)):
        result = read_txt("mock_path.txt")
        assert result == sample_txt_data, (
            f"Expected {sample_txt_data}, but got {result}"
        )


def test_save_txt(mock_state):
    """Test that the save_txt function writes the correct content to a file."""
    with mock.patch("builtins.open", mock.mock_open()) as mock_file:
        save_txt(mock_state)

        mock_file().write.assert_called_once()
        written_content = mock_file().write.call_args[0][0]

        assert "Patient Information:" in written_content
        assert "Medical Conditions:" in written_content
        assert "Diabetes" in written_content
        assert "E11.9" in written_content
        assert "Asthma" in written_content
        assert "J45" in written_content
