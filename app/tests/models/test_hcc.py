import pytest
from pydantic import ValidationError
from app.src.models.hcc import HCC  

def test_hcc_creation_valid_data():
    """Test creating a valid instance of the HCC model"""
    hcc_data = {
        "code": "A123",
        "description": "Test description",
        "tags": "test, example"
    }

    hcc = HCC(**hcc_data)

    assert hcc.code == "A123"
    assert hcc.description == "Test description"
    assert hcc.tags == "test, example"

def test_hcc_creation_with_optional_fields():
    """Test creating an instance of the HCC model with optional fields set to None"""
    hcc_data = {
        "code": "B456"
    }

    hcc = HCC(**hcc_data)

    assert hcc.code == "B456"
    assert hcc.description is None
    assert hcc.tags is None

def test_hcc_invalid_data_missing_required_field():
    """Test that the 'code' field is required"""
    hcc_data = {
        "description": "Missing code",
        "tags": "test"
    }

    with pytest.raises(ValidationError):
        HCC(**hcc_data)

def test_hcc_invalid_data_wrong_type():
    """Test that the 'code' field must be a string"""
    hcc_data = {
        "code": 123,  
        "description": "Invalid type for code",
        "tags": "test"
    }

    with pytest.raises(ValidationError):
        HCC(**hcc_data)
