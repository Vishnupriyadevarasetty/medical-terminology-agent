# Unit Test Report
Testing was performed throughout the development of the project to ensure that each component behaved as expected.

# Test Framework
The following tools were used during testing:
-pytest
-pytest-mock
-pytest-cov

# Test Coverage
Unit tests were written for all major modules in the project
The following files are covered:
-MedicalTerminologyAgent
-BedrockService
-InputValidator
-Exception classes
-Response model

The tests verify both successful execution and failure scenarios.

# Test Scenarios
The following scenarios were tested:
-Valid medical terminology
-Medical abbreviations
-Empty input
-Unknown medical terms
-Amazon Bedrock failure
-Local knowledge base fallback
-Custom exception handling

# Results
All unit tests completed successfully without failures.