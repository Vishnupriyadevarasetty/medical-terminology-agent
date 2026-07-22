# Medical Terminology Agent

# Introduction
The Medical Terminology Agent is an AI application that explains common medical terms in simple and easy-to-understand language. It is built using Python and Amazon Bedrock (Nova Micro) and is deployed on Amazon Bedrock AgentCore Runtime.

The application is designed for educational purposes only. It does not diagnose medical conditions or recommend treatments or medications.


# Technologies Used
- Python
- Amazon Bedrock
- Amazon Nova Micro
- Amazon Bedrock AgentCore Runtime
- Docker
- AWS CodeBuild
- Amazon ECR
- Amazon S3
- Amazon CloudWatch Logs
- GitHub Actions
- Pytest


# Project Structure
```text
medical_terminology_agent/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docs/
│
├── src/
│   └── medical_terminology_agent/
│       ├── agent.py
│       ├── bedrock_service.py
│       ├── exceptions.py
│       ├── knowledge_base.py
│       ├── logger.py
│       ├── models.py
│       └── validator.py
│
├── tests/
│
├── Dockerfile
├── main.py
├── run.py
├── requirements.txt
├── pytest.ini
└── README.md
```

# How It Works
1. The user enters a medical term.
2. The input is validated.
3. The request is sent to Amazon Bedrock.
4. Amazon Bedrock generates an explanation in simple language.
5. If Amazon Bedrock is unavailable, the application uses the local knowledge base.
6. The explanation is returned to the user.


# Features
- Explains common medical terminology in simple language.
- Uses Amazon Bedrock Nova Micro to generate responses.
- Validates user input before processing.
- Falls back to a local knowledge base if Bedrock is unavailable.
- Includes structured logging and exception handling.
- Containerized using Docker.
- Deployable on Amazon Bedrock AgentCore Runtime.
- Includes automated unit tests with 100% code coverage.
- Uses GitHub Actions for build and test automation.

# Running the Application
Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application locally.

```bash
python run.py
```

# Running Tests
Execute all unit tests.

```bash
pytest
```

Generate the code coverage report.

```bash
pytest --cov=medical_terminology_agent --cov-report=term-missing
```

# Deployment
The project can be deployed to Amazon Bedrock AgentCore Runtime using the AgentCore CLI.
Deployment flow:

1. Prepare the application for deployment.
2. Run the AgentCore deployment command.
3. AWS CodeBuild builds the application container.
4. The container image is stored in Amazon ECR.
5. Amazon Bedrock AgentCore Runtime is updated.
6. CloudWatch logs are available for monitoring and troubleshooting.

Deploy the latest version.

```bash
agentcore deploy
```

Check the runtime status.

```bash
agentcore status
```

# Running with AgentCore
Check the runtime status.

```bash
agentcore status
```

Invoke the deployed runtime.

```bash
agentcore invoke "{\"prompt\":\"Explain ECG\"}"
```

Example response:

```json
{
  "success": true,
  "category": "Medical Terminology",
  "message": "An ECG (Electrocardiogram) is a test that records the electrical activity of the heart."
}
```

# Execution Steps
Typical execution flow:

```bash
git clone <repository-url>

cd medical_terminology_agent

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python run.py

pytest

pytest --cov=medical_terminology_agent --cov-report=term-missing

agentcore deploy

agentcore status

agentcore invoke "{\"prompt\":\"Explain MRI\"}"
```

# Documentation
Additional project documentation is available in the docs folder.
- agent_design.md
- architecture.md
- agent_flow.md
- cicd.md
- execution_steps.md
- edge_cases.md
- unit_test_report.md


## Note
This project is intended for educational purposes only. The information provided by the application should not be considered medical advice or used for diagnosis or treatment decisions.