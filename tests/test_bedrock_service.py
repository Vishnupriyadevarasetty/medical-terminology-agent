import json

from medical_terminology_agent.bedrock_service import BedrockService


def test_explain_term_success(mocker):
    mock_client = mocker.Mock()

    mock_response = {
        "output": {
            "message": {
                "content": [
                    {
                        "text": "Diabetes is a blood sugar disorder."
                    }
                ]
            }
        }
    }

    mock_client.invoke_model.return_value = {
        "body": mocker.Mock(
            read=lambda: json.dumps(mock_response)
        )
    }

    mocker.patch(
        "boto3.client",
        return_value=mock_client,
    )

    service = BedrockService()

    result = service.explain_term("diabetes")

    assert "blood sugar" in result