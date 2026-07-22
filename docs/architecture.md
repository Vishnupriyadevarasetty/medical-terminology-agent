# System Architecture
-The Medical Terminology Agent follows a simple layered architecture.The user interacts with the AgentCore Runtime,which forwards the request to the application.
-The application validates the input and requests an explanation from Amazon Bedrock.If Bedrock is unavailable,it retrieves the explanation from the local knowledge base instead.

mermaid
flowchart TD

    User["User"]
    Runtime["Amazon Bedrock AgentCore Runtime"]
    Main["main.py"]
    Agent["MedicalTerminologyAgent"]
    Bedrock["Amazon Bedrock"]
    Nova["Amazon Nova Micro"]
    KB["Local Knowledge Base"]
    User --> Runtime
    Runtime --> Main
    Main --> Agent
    Agent --> Bedrock
    Bedrock --> Nova
    Nova --> Agent
    Agent -.Fallback.- KB
    Agent --> Runtime
    Runtime --> User
    
This design keeps the business logic independent from the deployment layer and allows the application to continue working even when the cloud model is temporarily unavailable.