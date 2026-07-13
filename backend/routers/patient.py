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
@router.get("/")
def get_patients():
    return[]

@router.post("",response_model=PatientResponse)
def create_patient(patient:PatientCreate):
    return patient