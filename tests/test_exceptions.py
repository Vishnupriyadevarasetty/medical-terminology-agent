import pytest

from medical_terminology_agent.exceptions import (
    InvalidQuestionError,
    MedicalTermNotFoundError,
)

def test_invalid_question_error():
    with pytest.raises(InvalidQuestionError):
        raise InvalidQuestionError("Invalid question")

def test_medical_term_not_found_error():
    with pytest.raises(MedicalTermNotFoundError):
        raise MedicalTermNotFoundError("Term not found")