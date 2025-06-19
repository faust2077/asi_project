"""Project pipelines."""

from kedro.pipeline import Pipeline
from your_project_name.pipelines import preprocessing, model_training

def register_pipelines() -> dict[str, Pipeline]:
    """Rejestracja wszystkich pipeline'ów"""
    
    preprocessing_pipeline = preprocessing.create_pipeline()
    model_training_pipeline = model_training.create_pipeline()
    
    return {
        "preprocessing": preprocessing_pipeline,
        "model_training": model_training_pipeline,
        "__default__": preprocessing_pipeline + model_training_pipeline,
    }
