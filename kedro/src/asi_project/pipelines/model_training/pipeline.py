from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
  setup_pycaret_experiment,
  compare_models_performance,
  tune_top_models,
  compare_tuned_models,
  finalize,
  save_model_artifacts
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=setup_pycaret_experiment,
            inputs=["preprocessed_calories","params:target_column","params:train_size","params:session_id"],
            outputs="pycaret_experiment",
            name="setup_experiment_node"
        ),
        node(
            func=compare_models_performance,
            inputs=["pycaret_experiment","params:n_models"],
            outputs="top_models",
            name="compare_models_node"
        ),
        node(
            func=tune_top_models,
            inputs="top_models",
            outputs="tuned_models",
            name="tune_models_node"
        ),
        node(
            func=compare_tuned_models,
            inputs="tuned_models",
            outputs="best_model",
            name="select_best_model_node"
        ),
        node(
            func=finalize,
            inputs="best_model",
            outputs="final_model",
            name="finalize_node"
        ),
        node(
            func=save_model_artifacts,
            inputs=["final_model","params:model_save_path"],
            outputs=None,
            name="save_model_node"
        )
    ])

