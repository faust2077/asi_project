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

def add_bmi_feature(df: pd.DataFrame) -> pd.DataFrame:
    """Dodaje kolumnę BMI"""
    df = df.copy()
    df["BMI"] = df["Weight"] / (df["Height"] / 100) ** 2
    return df

def detect_outliers_iqr(df: pd.DataFrame, target_column: str = 'Calories', 
                       factor: float = 1.5) -> Dict[str, Any]:
    """Wykrywa outliers metodą IQR i zwraca statystyki"""
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    numerical_columns = [col for col in numerical_columns if col != target_column]

    outliers_summary = {}
    for col in numerical_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        percent = len(outliers) / len(df) * 100
        outliers_summary[col] = {
            'count': len(outliers),
            'percent': round(percent, 2),
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
    
    return outliers_summary

def select_features_by_mutual_info(df: pd.DataFrame, target_column: str = 'Calories', 
                                 top_features: int = 5) -> pd.DataFrame:
    """Selekcja cech na podstawie mutual information"""
    X = df.drop(columns=target_column)
    y = df[target_column]
    
    # Encode categorical variables
    X_enc = X.copy()
    for col in X_enc.select_dtypes(include='object'):
        X_enc[col] = LabelEncoder().fit_transform(X_enc[col])
    
    # Calculate mutual information
    mi_scores = mutual_info_regression(X_enc, y, random_state=42)
    mi_series = pd.Series(mi_scores, index=X_enc.columns).sort_values(ascending=False)
    
    # Select top features + target
    selected_features = mi_series.head(top_features).index.tolist()
    selected_features.append(target_column)
    
    return df[selected_features]
