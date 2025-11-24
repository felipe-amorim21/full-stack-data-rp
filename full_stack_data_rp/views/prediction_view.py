from fastapi import APIRouter, HTTPException
from full_stack_data_rp.schemas.student_schema import StudentInput, PredictionOutput
from full_stack_data_rp.controllers.prediction_controller import predict_evasion

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": True}

@router.post("/predict", response_model=PredictionOutput)
def predict_student(student: StudentInput):
    try:
        return predict_evasion(student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))