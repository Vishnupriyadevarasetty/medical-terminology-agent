from dotenv import load_dotenv

load_dotenv()

from medical_terminology_agent.agent import MedicalTerminologyAgent
from medical_terminology_agent.exceptions import (
    InvalidQuestionError,
    MedicalTermNotFoundError,
)


def main()->None:
    agent=MedicalTerminologyAgent()
    question=input("Enter a medical term: ")

    try:
        response=agent.explain(question)
        print("\nResponse")
        print(f"Success :{response.success}")
        print(f"Category:{response.category}")
        print(f"Message :{response.message}")

    except InvalidQuestionError as error:
        print(f"\nValidation Error:{error}")

    except MedicalTermNotFoundError as error:
        print(f"\nLookup Error:{error}")

if __name__ =="__main__":
    main()