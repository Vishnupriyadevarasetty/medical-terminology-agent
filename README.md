# Medical Terminology Agent

# Overview
Medical Terminology Agent is an AI-powered educational assistant built using Amazon Bedrock AgentCore Runtime.

It explains common medical terms in simple language and is intended for educational purposes only. The agent never diagnoses diseases or recommends treatments.

# Features
- Explains medical terminology
- Uses Amazon Bedrock (Nova Micro)
- Local knowledge base fallback
- Input validation
- Structured logging
- Exception handling
- Unit testing
- 100% code coverage
- GitHub Actions CI/CD
- Automatic deployment package upload to Amazon S3
- Amazon Bedrock AgentCore Runtime deployment

# Project Structure
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
│
├── tests/
│
├── main.py
├── run.py
├── requirements.txt
├── pytest.ini
└── README.md

# Technologies
- Python
- Amazon Bedrock
- Amazon Nova Micro
- Amazon Bedrock AgentCore Runtime
- GitHub Actions
- Amazon S3
- Pytest
- Coverage

# Running Locally
```bash
pip install -r requirements.txt
```

```bash
python run.py
```

# Running AgentCore Runtime
```bash
python main.py
```

# Testing
```bash
pytest
```

Coverage

```bash
pytest --cov=medical_terminology_agent
```

# CI/CD
Every push to the main branch automatically:

- installs dependencies
- executes unit tests
- verifies code coverage
- creates deployment package
- uploads deployment package to Amazon S3

# Runtime
Hosted using Amazon Bedrock AgentCore Runtime.

# Documentation

- docs/architecture.md
- docs/cicd.md
- docs/agent_flow.md

# Disclaimer
This application provides educational information only and should not be used for medical diagnosis or treatment.