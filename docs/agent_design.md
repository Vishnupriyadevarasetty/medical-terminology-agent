# Agent Design

# Objective

The goal of this project was to build an educational Medical Terminology Agent related to life sciences. The agent explains medical terms in simple language so that non-medical users can understand them easily.

The agent is not intended to diagnose diseases, recommend medicines, or provide medical advice.


# Design Approach

I wanted to keep the design simple and modular so that each component had a clear responsibility. This made the code easier to understand, test, and maintain.

The project is divided into the following components.

## MedicalTerminologyAgent

This acts as the main entry point for the application.

Its responsibilities include:

- Validating the user's input
- Requesting an explanation from Amazon Bedrock
- Handling fallback scenarios
- Returning a structured response object


## BedrockService

I created a separate service class for Amazon Bedrock so that all model-related logic remains in one place.

This class is responsible for:

- Creating the prompt
- Invoking the Amazon Nova Micro model
- Parsing the model response
- Returning the explanation to the agent

Keeping the Bedrock logic separate also made unit testing easier.


## Input Validation

Before processing a request, the input is validated.

The validator checks for:

- Empty input
- Input containing only whitespace
- Very long requests

This helps prevent unnecessary processing and improves the overall reliability of the application.


## Local Knowledge Base

A small local knowledge base was added as a fallback mechanism.

If Amazon Bedrock is unavailable because of network issues, service errors, or AWS configuration problems, the application can still explain a few commonly used medical terms.

This improves reliability and prevents complete failure when the external service is unavailable.


## Logging

Logging was added to make debugging and monitoring easier.

The application logs:

- Incoming requests
- Successful responses
- Fallback execution
- Unexpected errors


## Error Handling

Custom exceptions were added to make failures easier to understand.

For example:

- Invalid input raises `InvalidQuestionError`
- Unknown medical terms raise `MedicalTermNotFoundError`

Using custom exceptions makes the code easier to read and maintain compared to handling generic exceptions.


## Configuration

AWS configuration is managed through environment variables instead of hardcoding values.

This allows the same application to run locally, during testing, and inside Amazon Bedrock AgentCore Runtime without modifying the source code.

The Bedrock model ID and AWS Region can be configured through environment variables, making the application easier to deploy across different environments.