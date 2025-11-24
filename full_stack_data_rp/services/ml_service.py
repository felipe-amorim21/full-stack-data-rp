import joblib
import pandas as pd
import os

class MLService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        model_path = "full_stack_data_rp/model/logistic_model.pkl"
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            raise FileNotFoundError(f"Modelo não encontrado em {model_path}")

    def predict_proba(self, data: pd.DataFrame) -> float:
        if not self.model:
            self.load_model()
        return self.model.predict_proba(data)[0][1]

ml_service = MLService()