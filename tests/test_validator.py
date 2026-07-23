import pytest

from medical_terminology_agent.exceptions import InvalidQuestionError
from medical_terminology_agent.validator import InputValidator

def test_validate_valid_question():
    assert InputValidator.validate("diabetes") is True

def test_validate_empty_question():
    with pytest.raises(InvalidQuestionError):
        InputValidator.validate("")

def test_validate_only_spaces():
    with pytest.raises(InvalidQuestionError):
        InputValidator.validate("     ")

def test_validate_question_too_long():
    long_question = "a"*201

    with pytest.raises(InvalidQuestionError):
        InputValidator.validate(long_question)