import json
import os

import boto3

class BedrockService:
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
        prompt = f"""
You are an educational Medical Terminology Assistant.

Your job is to explain only valid medical terminology.

You may explain:
- Diseases and medical conditions
- Human anatomy and organs
- Medical abbreviations (ECG, MRI, CBC, etc.)
- Laboratory tests
- Vitamins and minerals
- Medical procedures
- Medical terminology used in healthcare

Rules:
1. Explain only valid medical terms
2. Keep the explanation to 2-3 sentences
3. Do not diagnose diseases
4. Do not recommend treatments or medications
5. Do not answer general knowledge questions
6. If the input is not a medical term, respond only with:
"This does not appear to be a medical term. Please enter a valid medical term."

Medical term:
{medical_term}
"""

        request_body = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
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

        return response_body["output"]["message"]["content"][0]["text"]