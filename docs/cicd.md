# CI/CD Pipeline
A GitHub Actions workflow was created to automate the build and deployment process.
Whenever code is pushed to the 'main' branch,the workflow automatically performs several validation steps before creating the deployment package.

The pipeline performs the following activities:
1.Checks out the latest source code.
2.Installs all required dependencies.
3.Runs unit tests.
4.Verifies that code coverage is above the required threshold.
5.Creates a deployment ZIP file.
6.Uploads the deployment package to Amazon S3.

mermaid
flowchart LR

Developer --> GitHub
GitHub --> GitHubActions["GitHub Actions"]
GitHubActions --> Install["Install Dependencies"]
Install --> Test["Run Unit Tests"]
Test --> Coverage["Verify Code Coverage"]
Coverage --> Package["Create Deployment Package"]
Package --> S3["Amazon S3"]
S3 --> AgentCore["Amazon Bedrock AgentCore Runtime"]

Using this pipeline ensures that every deployment package is generated from tested code instead of relying on manual packaging.