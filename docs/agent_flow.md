# Agent Request Flow
The following sequence shows how a request is processed after a user submits a medical term.

mermaid
sequenceDiagram

User->>AgentCore Runtime:Submit medical term
AgentCore Runtime->>MedicalTerminologyAgent:explain(question)
MedicalTerminologyAgent->>InputValidator:Validate input
InputValidator-->>MedicalTerminologyAgent:Valid input
MedicalTerminologyAgent->>Amazon Bedrock:Request explanation
Amazon Bedrock-->>MedicalTerminologyAgent:Response
MedicalTerminologyAgent-->>AgentCore Runtime:MedicalResponse
AgentCore Runtime-->>User:Return explanation

If Amazon Bedrock is unavailable,the application attempts to retrieve the explanation from the local knowledge base before returning a response.
This flow keeps the interaction simple while ensuring the application can continue serving requests even when external services are unavailable.