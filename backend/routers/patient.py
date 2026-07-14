from fastapi import APIRouter
from schemas.patient import(
    PatientCreate,
    PatientResponse
)

from data.patient_data import patients

router=APIRouter(
    prefix="/patients",
    tags=["patients"]
)
@router.get("",response_model=list[PatientResponse])
def get_patients():
    return patients

@router.post("",response_model=PatientResponse)
def create_patient(patient:PatientCreate):
    new_patient={
        "id":len(patients)+1,
        **patient.model_dump()
    }
    patients.append(new_patient)
    return new_patient

@router.get("/{patient_id}",response_model=PatientResponse)
def get_patient(patient_id:int):
    for patient in patients:
        if patient["id"]==patient_id:
            return patient