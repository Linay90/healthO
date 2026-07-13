from fastapi import FastAPI
from routers.patient import router as patient_router 
app=FastAPI()
app.include_router(patient_router)