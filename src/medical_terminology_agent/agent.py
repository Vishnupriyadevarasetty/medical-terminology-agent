from medical_terminology_agent.bedrock_service import BedrockService
from medical_terminology_agent.exceptions import MedicalTermNotFoundError
from medical_terminology_agent.knowledge_base import MEDICAL_KNOWLEDGE
from medical_terminology_agent.logger import logger
from medical_terminology_agent.models import MedicalResponse
from medical_terminology_agent.validator import InputValidator


class MedicalTerminologyAgent:
    def __init__(self):
        self.bedrock_service=BedrockService()

    def explain(self, question:str) -> MedicalResponse:
        InputValidator.validate(question)

        search_term=question.strip().lower()
        logger.info("Searching for medical term: %s", search_term)

        try:
            explanation=self.bedrock_service.explain_term(search_term)

            logger.info("Medical term explained using Amazon Bedrock")

            return MedicalResponse(
                success=True,
                category="Medical Terminology",
                message=explanation,
            )

        except Exception as error:
            logger.warning(
                "Bedrock unavailable. Falling back to local knowledge base. %s",
                error,
            )

            if search_term not in MEDICAL_KNOWLEDGE:
                logger.warning("Medical term not found: %s", search_term)
                raise MedicalTermNotFoundError(
                    f"Medical term '{question}' was not found."
                )

            result=MEDICAL_KNOWLEDGE[search_term]

            logger.info("Medical term found in local knowledge base")

            return MedicalResponse(
                success=True,
                category=result["category"],
                message=result["description"],
            )