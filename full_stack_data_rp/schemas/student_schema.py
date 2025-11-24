from pydantic import BaseModel

class StudentInput(BaseModel):
    idade: int
    sexo: str
    tipo_escola_medio: str
    nota_enem: float
    renda_familiar: float
    trabalha: int
    horas_trabalho_semana: int
    reprovacoes_1_sem: int
    bolsista: int
    distancia_campus_km: float

    class Config:
        json_schema_extra = {
            "example": {
                "idade": 19,
                "sexo": "F",
                "tipo_escola_medio": "publica",
                "nota_enem": 650.5,
                "renda_familiar": 2.0,
                "trabalha": 1,
                "horas_trabalho_semana": 30,
                "reprovacoes_1_sem": 2,
                "bolsista": 0,
                "distancia_campus_km": 12.3
            }
        }

class PredictionOutput(BaseModel):
    prob_evasao: float
    classe_prevista: int
    threshold: float = 0.5