# Edge Cases
While developing the application,I considered a few situations where the agent could fail or receive unexpected input.These cases were handled to make the application more reliable.

# Empty Input
If the user presses Enter without typing anything, the application raises an 'InvalidQuestionError'.This prevents unnecessary processing.

# Whitespace Input
Inputs containing only spaces are treated as empty input and are rejected during validation.

# Unknown Medical Term
If the requested medical term is not available and Amazon Bedrock cannot generate a response,the application raises a 'MedicalTermNotFoundError'.This gives a meaningful error instead of returning incorrect information.

# Amazon Bedrock Unavailable
Network failures or temporary service issues are possible when using cloud services.To handle this situation,the application falls back to the local knowledge base whenever possible.This allows commonly known medical terms to continue working even if Bedrock is unavailable.

# Invalid AWS Configuration
If incorrect AWS credentials or region settings are provided,Bedrock requests will fail.
The error is logged, and the fallback mechanism is attempted before returning an error to the user.

# Unexpected Errors
Although the application handles the expected scenarios,unexpected runtime errors are also logged.This makes troubleshooting easier without exposing internal implementation details to the user.