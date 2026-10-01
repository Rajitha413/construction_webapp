import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_model():

    df = pd.read_csv("data/construction_material_forecast_balanced1.csv")

    X = df[['Area_sqft','Building_Floors','Duration_days','Workers']]
    y = df[['Cement_bags','Steel_tons','Bricks_units','Asphalt_tons']]

    model = joblib.load("model/material_model.pkl")
    scaler = joblib.load("model/scaler.pkl")

    X_scaled = scaler.transform(X)
    y_pred = model.predict(X_scaled)

    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    return mae, rmse, r2