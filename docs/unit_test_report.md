# Unit Test Report
Unit testing was performed during development to verify that each component of the application worked as expected. The tests cover both normal execution and common failure scenarios.


# Test Framework
The following tools were used for testing:
- pytest
- pytest-mock
- pytest-cov

# Test Coverage
Unit tests were written for the main components of the application, including:
- MedicalTerminologyAgent
- BedrockService
- InputValidator
- Custom exception classes
- MedicalResponse model

The tests verify both successful execution and error handling.

# Test Scenarios
The following scenarios were tested:
- Valid medical terms
- Medical abbreviations
- Empty input
- Input containing only whitespace
- Unknown medical terms
- Amazon Bedrock service failure
- Local knowledge base fallback
- Custom exception handling

# Test Results
A total of **13 unit tests** were executed successfully.
No test failures were observed during the final test execution.