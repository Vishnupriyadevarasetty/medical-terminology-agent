"""
Custom exceptions for the Medical Terminology Agent.
"""


class InvalidQuestionError(Exception):
    """
    Raised when the user's question is invalid.
    """


class MedicalTermNotFoundError(Exception):
    """
    Raised when the requested medical term is not found.
    """