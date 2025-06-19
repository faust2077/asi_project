from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    drop_user_id,
    remove_empty_rows, 
    remove_duplicates,
    add_bmi_feature,
    detect_outliers_iqr,
    select_features_by_mutual_info
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
            func=add_bmi_feature,
            inputs="calories_no_duplicates",
            outputs="calories_with_bmi", 
            name="add_bmi_node"
        ),
        node(
            func=detect_outliers_iqr,
            inputs=["calories_with_bmi", "params:target_column"],
            outputs="outliers_report",
            name="detect_outliers_node"
        ),
        node(
            func=select_features_by_mutual_info,
            inputs=["calories_with_bmi", "params:target_column", "params:top_features"],
            outputs="preprocessed_calories",
            name="feature_selection_node"
        )
    ])
