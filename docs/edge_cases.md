# Edge Cases
While developing the application, I considered a few situations where the agent might receive unexpected input or encounter failures. These cases were handled to make the application more reliable.


# Empty Input

If the user presses **Enter** without typing anything, the application raises an `InvalidQuestionError`. This prevents unnecessary processing of invalid requests.

# Whitespace Input
If the input contains only spaces or tabs, it is treated as empty input and is rejected during validation.

# Unknown Medical Term
If the requested medical term is not available in the local knowledge base and Amazon Bedrock is unable to generate a response, the application raises a `MedicalTermNotFoundError`. This helps return a meaningful error instead of incorrect information.

# Amazon Bedrock Unavailable
Temporary network issues or service interruptions may prevent Amazon Bedrock from responding.

In this situation, the application attempts to retrieve the explanation from the local knowledge base. This allows commonly used medical terms to continue working even when Bedrock is unavailable.


# Invalid AWS Configuration
If incorrect AWS credentials, region settings, or model configuration are provided, Amazon Bedrock requests will fail.

The application logs the error and attempts to use the local knowledge base before returning an error to the user.


# Unexpected Errors
Although the application handles the expected scenarios, unexpected runtime errors can still occur.

Such errors are logged to make troubleshooting easier while avoiding the exposure of internal application details to the user.