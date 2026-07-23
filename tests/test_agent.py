import pytest

from medical_terminology_agent.agent import MedicalTerminologyAgent
from medical_terminology_agent.exceptions import (
    InvalidQuestionError,
    MedicalTermNotFoundError,
)

def test_explain_valid_disease(mocker):
    mocker.patch(
        "medical_terminology_agent.agent.BedrockService.explain_term",
        return_value="Diabetes is a condition related to high blood sugar levels",
    )

    agent=MedicalTerminologyAgent()
    response=agent.explain("diabetes")

    assert response.success is True
    assert response.category=="Medical Terminology"
    assert "blood sugar" in response.message


def test_explain_valid_abbreviation(mocker):
    mocker.patch(
        "medical_terminology_agent.agent.BedrockService.explain_term",
        return_value="ECG (Electrocardiogram) records heart activity",
    )

    agent=MedicalTerminologyAgent()
    response=agent.explain("ecg")

    assert response.success is True
    assert "Electrocardiogram" in response.message

def test_explain_fallback_to_knowledge_base(mocker):
    mocker.patch(
        "medical_terminology_agent.agent.BedrockService.explain_term",
        side_effect=Exception("Bedrock unavailable"),
    )

    agent=MedicalTerminologyAgent()
    response=agent.explain("diabetes")

    assert response.success is True
    assert response.category=="Disease"
    assert "blood" in response.message.lower()

def test_explain_unknown_term(mocker):
    mocker.patch(
        "medical_terminology_agent.agent.BedrockService.explain_term",
        side_effect=Exception("Bedrock unavailable"),
    )

    agent=MedicalTerminologyAgent()
    with pytest.raises(MedicalTermNotFoundError):
        agent.explain("unknown_term")

def test_explain_empty_question():
    agent=MedicalTerminologyAgent()
    with pytest.raises(InvalidQuestionError):
        agent.explain("")