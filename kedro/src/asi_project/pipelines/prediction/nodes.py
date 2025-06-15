import os
import pandas as pd
import logging
from pycaret.regression import load_model, predict_model

logging = logging.getLogger(__name__)

def prepare_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare input data for prediction by removing specified columns.

    Args:
        raw_data: Raw input dataframe

    Returns:
        Processed dataframe ready for prediction
    """
    df = raw_df.copy()
    columns_to_drop = ['Gender', 'Height', 'Weight', 'Age']

    existing_columns = [col for col in columns_to_drop if col in df.columns]

    # only drop columns that exist within the table
    if existing_columns:
        df.drop(columns=existing_columns, inplace=True)

    return df


def load_trained_model(model_name: str):
    """
    Load the trained PyCaret model.
    
    Args:
        model_name: Name of the model file (without extension)
        
    Returns:
        Loaded PyCaret model
    """
    # Load from data catalog path
    model_path = f"data/06_models/{model_name}"
    
    model = load_model(model_path)
    return model


def use_model(prepared_df: pd.DataFrame, model_path: str) -> pd.DataFrame:
    """
    Make predictions using the trained model.

    Args:
        prepared_data: Preprocessed data ready for prediction
        model_path: Path to the trained model

    Returns:
        DataFrame with predictions
    """
    df = prepare_data(dataframe)

    model = load_model(model_path)
    predictions = predict_model(model, data=prepared_df)
    y_pred = predictions['prediction_label']

    logger.info(f"Generated {len(predictions)} predictions")

    return y_pred.iloc[0].round(0)
