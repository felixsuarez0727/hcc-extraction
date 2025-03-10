from src.agents.medical_conditions_agent.prompts.extraction_prompts import EXTRACTION_PROMPTS


def test_prompts_keys():
    """Test that the EXTRACTION_PROMPTS dictionary has the correct keys."""
    assert "patient_information_prompt" in EXTRACTION_PROMPTS
    assert "medical_conditions_prompt" in EXTRACTION_PROMPTS


def test_prompts_values():
    """Test that the prompts are strings and have content."""
    assert isinstance(EXTRACTION_PROMPTS["patient_information_prompt"], str)
    assert isinstance(EXTRACTION_PROMPTS["medical_conditions_prompt"], str)
    assert len(EXTRACTION_PROMPTS["patient_information_prompt"]) > 0
    assert len(EXTRACTION_PROMPTS["medical_conditions_prompt"]) > 0
