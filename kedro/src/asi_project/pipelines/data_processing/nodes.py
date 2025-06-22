import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression
from sklearn.preprocessing import LabelEncoder
from typing import Dict, Any

def drop_user_id(df: pd.DataFrame) -> pd.DataFrame:
    """Usuwa kolumnę User_ID z DataFrame"""
    return df.drop(columns=["User_ID"])

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Usuwa wiersze z pustymi komórkami"""
    return df.dropna()

def remove_duplicates(df: pd.DataFrame, target_column: str = 'Calories') -> pd.DataFrame:
    """Usuwa duplikaty pełne i częściowe"""
    # Usuń pełne duplikaty
    df = df.drop_duplicates()
    
    # Usuń częściowe duplikaty (te same cechy, różny target)
    feature_cols = [col for col in df.columns if col != target_column]
    partial_duplicate_mask = df.duplicated(subset=feature_cols, keep=False)
    df = df.drop(index=df[partial_duplicate_mask].index)
    
    return df

def keep_selected_features(df: pd.DataFrame) -> pd.DataFrame:
    """Zostawia tylko wybrane cechy w DataFrame"""
    selected_features = ['Duration', 'Body_Temp', 'Heart_Rate', 'Age', 'Gender', 'Calories']
    return df[selected_features]

