from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    setup_pycaret_experiment,
    compare_models_performance, 
    create_and_tune_best_model,
    evaluate_model_performance,
    finalize_and_predict,
    save_model_artifacts
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=setup_pycaret_experiment,
            inputs=["preprocessed_calories", "params:target_column", 
                   "params:train_size", "params:session_id"],
            outputs="pycaret_experiment",
            name="setup_experiment_node"
        ),
        node(
            func=compare_models_performance, 
            inputs=["pycaret_experiment", "params:n_models"],
            outputs="model_comparison",
            name="compare_models_node"
        ),
        node(
            func=create_and_tune_best_model,
            inputs=["pycaret_experiment", "params:best_model_name"],
            outputs="tuned_model",
            name="create_tune_model_node"
        ),
        node(
            func=evaluate_model_performance,
            inputs="tuned_model",
            outputs="model_metrics",
            name="evaluate_model_node"
        ),
        node(
            func=finalize_and_predict,
            inputs="tuned_model",
            outputs=["final_model", "predictions"],
            name="finalize_predict_node"
        ),
        node(
            func=save_model_artifacts,
            inputs=["final_model", "params:model_save_path"],
            outputs=None,
            name="save_model_node"
        )
    ])
