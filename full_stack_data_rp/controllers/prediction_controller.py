import pandas as pd
from full_stack_data_rp.services.ml_service import ml_service
from full_stack_data_rp.schemas.student_schema import StudentInput, PredictionOutput

def predict_evasion(student_data: StudentInput) -> PredictionOutput:
    # Converter Pydantic model para DataFrame
    input_df = pd.DataFrame([student_data.model_dump()])
    
    # Obter probabilidade
    proba = ml_service.predict_proba(input_df)
    
    # Aplicar Threshold [cite: 167]
    threshold = 0.5
    classe = 1 if proba >= threshold else 0
    
    return PredictionOutput(
        prob_evasao=round(proba, 4),
        classe_prevista=classe,
        threshold=threshold
    )