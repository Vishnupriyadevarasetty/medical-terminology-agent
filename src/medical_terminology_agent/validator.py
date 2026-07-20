"""
Input validation for the Medical Terminology Agent.
"""

from medical_terminology_agent.exceptions import InvalidQuestionError


class InputValidator:
    """
    Validates user input before it is processed by the agent.
    """

    @staticmethod
    def validate(question: str) -> bool:
        """
        Validate the user's question.

        Args:
            question: The user's input.

        Returns:
            True if the input is valid.

        Raises:
            InvalidQuestionError: If the input is invalid.
        """
        if not question:
            raise InvalidQuestionError("Question cannot be empty.")

        if not question.strip():
            raise InvalidQuestionError("Question cannot contain only spaces.")

        if len(question) > 200:
            raise InvalidQuestionError("Question is too long.")

        return True