from pydantic import BaseModel,EmailStr
class PatientBase(BaseModel):
    first_name:str
    last_name:str
    age:int 
    email:EmailStr

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id:int