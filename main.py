from bedrock_agentcore import BedrockAgentCoreApp

from medical_terminology_agent.agent import MedicalTerminologyAgent
from medical_terminology_agent.exceptions import MedicalTermNotFoundError


app = BedrockAgentCoreApp()

agent = None


def get_agent():
    global agent

    if agent is None:
        agent = MedicalTerminologyAgent()

    return agent


@app.entrypoint
def invoke(payload):
    try:
        print("RECEIVED PAYLOAD:", payload)

        question = ""

        if isinstance(payload, dict):
            # Case 1: {"question": "..."}
            question = payload.get("question", "")

            # Case 2: {"input": {"question": "..."}}
            if not question:
                input_data = payload.get("input", {})
                if isinstance(input_data, dict):
                    question = input_data.get("question", "")

        # Case 3: plain string payload
        if not question and isinstance(payload, str):
            question = payload

        response = get_agent().explain(question)

        return {
            "success": response.success,
            "category": response.category,
            "message": response.message,
        }

    except MedicalTermNotFoundError as error:
        return {
            "success": False,
            "message": str(error),
        }

    except Exception as error:
        print("ERROR:", error)

        return {
            "success": False,
            "message": f"Unexpected error: {error}",
        }


if __name__ == "__main__":
    invoke.run()