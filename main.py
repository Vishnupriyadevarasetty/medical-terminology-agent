from bedrock_agentcore import BedrockAgentCoreApp

from medical_terminology_agent.agent import MedicalTerminologyAgent
from medical_terminology_agent.exceptions import MedicalTermNotFoundError


app=BedrockAgentCoreApp()

agent=None


def get_agent():
    global agent

    if agent is None:
        agent=MedicalTerminologyAgent()

    return agent


@app.entrypoint
def invoke(payload):

    try:
        question=(
            payload.get("question")
            or payload.get("prompt")
            or ""
        )

        response=get_agent().explain(question)

        return {
            "success":response.success,
            "category":response.category,
            "message":response.message,
        }

    except MedicalTermNotFoundError as error:

        return {
            "success":False,
            "message":str(error),
        }

    except Exception as error:

        return {
            "success":False,
            "message":f"Unexpected error: {error}",
        }


if __name__ == "__main__":
    app.run()