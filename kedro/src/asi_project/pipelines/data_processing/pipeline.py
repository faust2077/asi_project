from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    drop_user_id,
    remove_empty_rows, 
    remove_duplicates,
    keep_selected_features,    
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=drop_user_id,
            inputs="raw_calories",
            outputs="calories_no_user_id",
            name="drop_user_id_node"
        ),
        node(
            func=remove_empty_rows,
            inputs="calories_no_user_id", 
            outputs="calories_no_empty",
            name="remove_empty_rows_node"
        ),
        node(
            func=remove_duplicates,
            inputs=["calories_no_empty", "params:target_column"],
            outputs="calories_no_duplicates",
            name="remove_duplicates_node"
        ),
        node(
            func=keep_selected_features,
            inputs="calories_no_duplicates",
            outputs="calories_selected_features",
            name="keep_selected_features_node"
        ),
    ])
