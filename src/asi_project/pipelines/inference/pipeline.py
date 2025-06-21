from kedro.pipeline import Pipeline, node
from .nodes import load_model_node, predict_node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=load_model_node,
                inputs=None,
                outputs="model",
                name="load_model_node",
            ),
            node(
                func=predict_node,
                inputs=["preprocessed_calories", "model"],
                outputs="predictions",
                name="predict_node",
            ),
        ]
    )

