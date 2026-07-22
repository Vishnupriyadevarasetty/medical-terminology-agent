# Agent Design

# Objective
The goal of this project was to build an educational Medical Terminology Agent related to life sciences.The agent should explain medical terms in simple language so that non-medical users can understand them easily.
-The agent is not intended to diagnose diseases,recommend medicines,orprovide medical advice.

# Design Approach
I wanted to keep the design simple and modular so that each component had a clear responsibility.This made the code easier to test and maintain.
The project was divided into the following parts:
MedicalTerminologyAgent-
This acts as the main entry point for the application.
Its responsibilities are:
-validating the user's question
-requesting an explanation from Amazon Bedrock
-handling failures
-returning a structured response object

# BedrockService
I created a separate service class for Amazon Bedrock so that all model-related logic stays in one place.
This class contains:
-creates the prompt
-invokes the Nova Micro model
-parses the response
-returns the explanation back to the agent
Keeping Bedrock logic separate also made unit testing easier.

# Input Validation
Before processing a request,the input is validated.
This prevents issues such as:
-empty strings
-whitespace-only input
-invalid requests

# Local Knowledge Base
A small local knowledge base was added as a fallback mechanism
If Bedrock is unavailable because of network issues,service errors,or invalid AWS configuration,the application can still answer some commonly known medical terms.
This improves reliability and prevents complete failure.

# Logging
Logging was added to make debugging easier
The application logs:
-incoming requests
-successful responses
-fallback execution
-unexpected failures

# Error Handling
Custom exceptions were added to make failures easier to understand.
For example:
-invalid input raises 'InvalidQuestionError'
-unknown medical terms raise 'MedicalTermNotFoundError'

This provides cleaner error handling compared to generic exceptions.

# Configuration
AWS configuration is managed through environment variables instead of hardcoding values.
This allows the same code to run locally, in CI/CD pipelines, and inside AgentCore Runtime without changing the source code.