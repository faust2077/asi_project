from .pipelines import data_processing, model_training

def register_pipelines():
    return {
        "__default__": (
            data_processing.create_pipeline()
            + model_training.create_pipeline()
        ),
        "data_processing": data_processing.create_pipeline(),
        "model_training": model_training.create_pipeline(),
    }

