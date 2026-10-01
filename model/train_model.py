import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("../data/construction_material_forecast_balanced1.csv")

# Handle Missing Values
df.fillna(df.mean(numeric_only=True), inplace=True)

X = df[['Area_sqft','Building_Floors','Duration_days','Workers']]
y = df[['Cement_bags','Steel_tons','Bricks_units','Asphalt_tons']]

# Train Test Split
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train Model
model = LinearRegression()
model.fit(X_train_scaled,y_train)

# Save Model
joblib.dump(model,"material_model.pkl")
joblib.dump(scaler,"scaler.pkl")

print("✅ Model trained and saved successfully")