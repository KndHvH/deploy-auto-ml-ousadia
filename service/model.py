import pandas as pd
from pycaret.classification import *

MODEL_PKL_PATH='./model/pickle_lightgbm_pycaret'
MODEL = load_model(MODEL_PKL_PATH)

def predict_on_data(data_file_path: str):
    X_test = pd.read_csv(data_file_path)
    return predict_model(MODEL, data = X_test, raw_score = True)

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)