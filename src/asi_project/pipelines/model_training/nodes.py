import pandas as pd
import numpy as np
from pycaret.regression import *
from typing import Dict, Any, Tuple
import pickle

def setup_pycaret_experiment(df: pd.DataFrame, target_column: str = 'Calories',
                            train_size: float = 0.8, session_id: int = 42) -> Any:
    """Konfiguruje eksperyment PyCaret"""
    exp = setup(
        data=df, 
        target=target_column,
        train_size=train_size,
        session_id=session_id,
        silent=True
    )
    return exp

def compare_models_performance(experiment: Any, n_models: int = 5) -> pd.DataFrame:
    """Porównuje wydajność różnych modeli"""
    best_models = compare_models(
        n_select=n_models,
        sort='MAE',
        verbose=False
    )
    return best_models

def create_and_tune_best_model(experiment: Any, model_name: str = 'lightgbm') -> Any:
    """Tworzy i strojuje najlepszy model"""
    # Stwórz model
    model = create_model(model_name, verbose=False)
    
    # Dostrojenie hiperparametrów  
    tuned_model = tune_model(model, verbose=False)
    
    return tuned_model

def evaluate_model_performance(model: Any) -> Dict[str, Any]:
    """Ewaluuje model na zbiorze testowym"""
    # Evaluate zwraca metryki jako dict
    metrics = pull()  # Ostatnie metryki z evaluate_model
    return metrics.to_dict()

def finalize_and_predict(model: Any, test_data: pd.DataFrame = None) -> Tuple[Any, pd.DataFrame]:
    """Finalizuje model i wykonuje predykcje"""
    # Finalizuj model (trenuj na pełnym zbiorze)
    final_model = finalize_model(model)
    
    # Wykonaj predykcje
    if test_data is not None:
        predictions = predict_model(final_model, data=test_data)
    else:
        predictions = predict_model(final_model)
    
    return final_model, predictions

def save_model_artifacts(model: Any, model_path: str) -> None:
    """Zapisuje wytrenowany model"""
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
