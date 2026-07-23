from dataclasses import dataclass


@dataclass
class MedicalResponse:
    success:bool
    message:str
    category:str