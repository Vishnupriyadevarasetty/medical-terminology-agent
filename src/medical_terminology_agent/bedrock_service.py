"""
Amazon Bedrock service for Medical Terminology Agent.
"""

import json
import os

import boto3


class BedrockService:
    """
    Handles communication with Amazon Bedrock.
    """

    def __init__(self):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=os.getenv("AWS_REGION", "us-east-1"),
        )

        self.model_id = os.getenv(
            "BEDROCK_MODEL_ID",
            "amazon.nova-micro-v1:0",
        )

    def explain_term(self, medical_term: str) -> str:
        """
        Generate a simple educational explanation for a medical term.
        """

        prompt = f"""
You are a Medical Terminology Assistant.

Your ONLY responsibility is explaining medical terminology.

Valid medical terminology includes:
- Diseases
- Medical conditions
- Human anatomy and organs
- Medical abbreviations (ECG, MRI, CBC, CT, etc.)
- Laboratory tests
- Vitamins and minerals
- Medical procedures
- Healthcare terminology

Instructions:

1. If the input IS a valid medical term:
   - Return ONLY the explanation.
   - Keep it to 2-3 simple sentences.
   - Do NOT diagnose.
   - Do NOT recommend treatment.
   - Do NOT add warnings.
   - Do NOT append any extra text.

2. If the input is NOT a valid medical term:
   Return EXACTLY this sentence and NOTHING ELSE:

This does not appear to be a medical term. Please enter a valid medical term.

Medical term:
{medical_term}
"""

        request_body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt,
                        }
                    ],
                }
            ]
        }

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(request_body),
            contentType="application/json",
            accept="application/json",
        )

        response_body = json.loads(response["body"].read())

        explanation = response_body["output"]["message"]["content"][0]["text"].strip()

        return explanation