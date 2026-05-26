from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Patient:
    id: int
    name: str
    vitals: Dict[str, Any]


class MockDatabase:
    def __init__(self):
        self.patients = {
            42: Patient(id=42, name="John", vitals={"heart_rate": 72, "blood_pressure": "120/80"}),
            101: Patient(id=101, name="Sarah", vitals={"heart_rate": 72, "blood_pressure": "120/80"})
        }

    def get_patient_name(self, patient_id: int) -> str:
        patient = self.patients.get(patient_id)
        return patient.name if patient else "Bilinmeyen Hasta"

    def get_latest_vitals(self, patient_id: int) -> Dict[str, Any]:
        patient = self.patients.get(patient_id)
        return patient.vitals if patient else {}
