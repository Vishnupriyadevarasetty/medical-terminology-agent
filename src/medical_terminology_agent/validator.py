from medical_terminology_agent.exceptions import InvalidQuestionError


class InputValidator:
    @staticmethod
    def validate(question: str) -> bool:
        if not question:
            raise InvalidQuestionError("Question cannot be empty.")

        if not question.strip():
            raise InvalidQuestionError("Question cannot contain only spaces.")

        if len(question) > 200:
            raise InvalidQuestionError("Question is too long.")

        return True