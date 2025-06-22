import os
from google.cloud import storage
from pycaret.regression import load_model, predict_model

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def prepare_data(dataframe, model):

    df = dataframe.copy()
    features = list(model.feature_names_in_)
    if 'Calories' in features:
        features.remove('Calories')

    return df

def use_model(dataframe):

    project_root = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir, os.pardir))
    model_path = os.path.join(project_root, 'data', '06_models', 'final_model')
    model = load_model(model_path)
    df = prepare_data(dataframe, model)

    predictions = predict_model(model, data=df)
    y_pred = predictions['prediction_label']

    return y_pred.iloc[0].round(0)
