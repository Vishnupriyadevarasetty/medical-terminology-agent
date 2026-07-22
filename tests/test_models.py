from medical_terminology_agent.models import MedicalResponse


def test_medical_response_creation():
    response = MedicalResponse(
        success=True,
        message="Sample explanation",
        category="Disease",
    )

    assert response.success is True
    assert response.message == "Sample explanation"
    assert response.category == "Disease"