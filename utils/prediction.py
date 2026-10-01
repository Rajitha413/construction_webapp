import pandas as pd
import joblib

model = joblib.load("model/material_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_materials(area,floors,duration,workers):

    new_data = pd.DataFrame({
        "Area_sqft":[area],
        "Building_Floors":[floors],
        "Duration_days":[duration],
        "Workers":[workers]
    })

    new_scaled = scaler.transform(new_data)
    prediction = model.predict(new_scaled)

    return {
        "Cement_bags":round(prediction[0][0],2),
        "Steel_tons":round(prediction[0][1],2),
        "Bricks_units":round(prediction[0][2],2),
        "Asphalt_tons":round(prediction[0][3],2)
    }