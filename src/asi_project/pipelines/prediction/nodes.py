import os
from pycaret.regression import load_model, predict_model

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def prepare_data(dataframe):

    df = dataframe.copy()
    df.drop(columns=['Gender', 'Height', 'Weight', 'Age'], inplace=True)

    return df

def use_model(dataframe):

    df = prepare_data(dataframe)

    model_path = os.path.join(SCRIPT_DIR, 'tuned_model_1')
    model = load_model(model_path)
    predictions = predict_model(model, data=df)
    y_pred = predictions['prediction_label']

    return y_pred.iloc[0].round(0)