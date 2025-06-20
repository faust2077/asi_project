"""Project pipelines."""

from kedro.pipeline import Pipeline
from asi_project.pipelines import data_processing, model_training

def register_pipelines() -> dict[str, Pipeline]:
    """Rejestracja wszystkich pipeline'ów"""
    
    data_processing_pipeline = data_processing.create_pipeline()
    model_training_pipeline = model_training.create_pipeline()
    
    return {
        "data_processing": data_processing_pipeline,
        "model_training": model_training_pipeline,
        "__default__": data_processing_pipeline + model_training_pipeline,
    }
