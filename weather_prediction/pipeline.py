import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from model import GDRegressor

FEATURE_COLUMNS = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"]
TARGET_COLUMN = "apparent_temperature"



def train_model(data: pd.DataFrame):
    """В этой функции описывается пайплайн обучения вашей модели линейной регрессии"""
    if data.empty:
        raise ValueError("Данных нет")

    X = data[FEATURE_COLUMNS]
    y = data[TARGET_COLUMN]

    # PUT YOUR CODE HERE

    return reg, {"MAE": mae, "RMSE": rmse, "R2": r2}, test_data, scaler
