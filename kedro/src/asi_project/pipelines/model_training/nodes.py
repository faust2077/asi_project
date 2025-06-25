import pandas as pd
import numpy as np
from pycaret.regression import *
from typing import List, Any, Tuple
import pickle

def setup_pycaret_experiment(df: pd.DataFrame, target_column: str = 'Calories',
                            train_size: float = 0.8, session_id: int = 42) -> Any:
    """Konfiguruje eksperyment PyCaret"""
    exp = setup(
        data=df, 
        target=target_column,
        normalize=True,
        transformation=True,
        session_id=session_id,
        verbose=True,
        train_size=train_size,
        fold=10,
        fold_shuffle=True
    )
    return exp


def compare_models_performance(experiment: Any, n_models: int = 3) -> List[Any]:
    top_models = compare_models(n_select=n_models)
    return top_models


def tune_top_models(models: List[Any]) -> List[Any]:
    tuned_models = [tune_model(m) for m in models]
    return tuned_models


def compare_tuned_models(tuned_models: List[Any]) -> Any:
    best_tuned_model = compare_models(tuned_models, sort='R2')
    return best_tuned_model


def finalize(model: Any, test_data: pd.DataFrame = None) -> Any:
    final_model = finalize_model(model)
    return final_model


def save_model_artifacts(model: Any, model_path: str) -> None:
    """Zapisuje wytrenowany model"""
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

