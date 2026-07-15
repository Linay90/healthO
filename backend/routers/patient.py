from fastapi import APIRouter,HTTPException 
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
        #"** is used for creating a new dictionary by unpacking another dictionary into it."   
    }
    patients.append(new_patient)
    return new_patient

@router.get("/{patient_id}",response_model=PatientResponse)
def get_patient(patient_id:int):
    for patient in patients:
        if patient["id"]==patient_id:
            return patient
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

@router.put("/{patient_id}",response_model=PatientResponse)
def update_patient(patient_id:int,patient:PatientCreate):
    for existing_patient in patients:
        if existing_patient["id"]==patient_id:
            existing_patient.update(patient.model_dump())
            return existing_patient
    raise HTTPException(
        status_code=404,
        detail="patient not found"
    )

@router.delete("/{patient_id}")
def delete_patient(patient_id:int):
    for index,patient in enumerate(patients):
        if patient["id"]==patient_id:
            patients.pop(index)
            return{
                "message":f"patient-deleted-{patient_id}"
            }
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
