"""
Unit tests for validator.py
"""

import pytest

from medical_terminology_agent.exceptions import InvalidQuestionError
from medical_terminology_agent.validator import InputValidator


def test_validate_valid_question():
    """
    Test that a valid question passes validation.
    """
    assert InputValidator.validate("diabetes") is True


def test_validate_empty_question():
    """
    Test that an empty question raises an exception.
    """
    with pytest.raises(InvalidQuestionError):
        InputValidator.validate("")


def test_validate_only_spaces():
    """
    Test that a question containing only spaces raises an exception.
    """
    with pytest.raises(InvalidQuestionError):
        InputValidator.validate("     ")


def test_validate_question_too_long():
    """
    Test that a very long question raises an exception.
    """
    long_question = "a" * 201

    with pytest.raises(InvalidQuestionError):
        InputValidator.validate(long_question)