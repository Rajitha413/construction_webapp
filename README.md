# 🏗️ Construction Material Requirement Forecasting

A Machine Learning-based web application that predicts construction material requirements using project parameters such as area, number of floors, project duration, and number of workers.

The system uses **Multi-Output Linear Regression** to predict:
- 🧱 Cement bags
- 🔩 Steel tons
- 🧱 Bricks units
- 🛣️ Asphalt tons

The predictions are presented through an interactive **Streamlit dashboard** with visualizations and a delay-risk indicator.

---

## 📌 Project Objective

Construction projects often face material estimation problems due to manual calculations and uncertain project conditions.

This project aims to:
- Predict required construction materials.
- Reduce manual estimation effort.
- Support construction planning.
- Visualize predicted material requirements.
- Provide a simple project delay-risk indication.

---

## 🧠 Machine Learning Approach

### Input Features

The model uses the following project parameters:

| Feature | Description |
|---|---|
| `Area_sqft` | Construction area in square feet |
| `Building_Floors` | Number of floors |
| `Duration_days` | Expected project duration |
| `Workers` | Number of workers |

### Output Targets

| Target | Description |
|---|---|
| `Cement_bags` | Required cement bags |
| `Steel_tons` | Required steel in tons |
| `Bricks_units` | Required number of bricks |
| `Asphalt_tons` | Required asphalt in tons |

### Algorithm

**Linear Regression** is used as the main machine learning algorithm.

The model is trained as a multi-output regression model to predict all four material requirements simultaneously.

---

## 🔄 Project Workflow

```text
Construction Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
Linear Regression Model
        ↓
Material Prediction
        ↓
Evaluation & Visualization
        ↓
Streamlit Dashboard
```

---

## 📂 Project Structure

```text
construction_webapp/
│
├── data/
│   └── construction_material_forecast_balanced1.csv
│
├── model/
│   ├── train_model.py
│   ├── material_model.pkl
│   └── scaler.pkl
│
├── utils/
│   ├── prediction.py
│   └── evaluation.py
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

### Folder/File Description

- **`data/`** – Contains the construction dataset.
- **`model/train_model.py`** – Trains the Linear Regression model and saves the model and scaler.
- **`model/material_model.pkl`** – Saved trained machine learning model.
- **`model/scaler.pkl`** – Saved StandardScaler used for preprocessing.
- **`utils/prediction.py`** – Loads the trained model and generates predictions.
- **`utils/evaluation.py`** – Contains model evaluation functionality.
- **`app.py`** – Main Streamlit web application.
- **`requirements.txt`** – Required Python libraries.
- **`README.md`** – Project documentation.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data handling and preprocessing
- **NumPy** – Numerical operations
- **Scikit-learn** – Machine learning and evaluation
- **Matplotlib** – Data visualization
- **Joblib** – Saving and loading trained models
- **Streamlit** – Web application and dashboard

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd construction_webapp
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib joblib
```

---

## 🚀 How to Run

### Step 1: Train the Model

If the model files are not already present:

```bash
python model/train_model.py
```

This creates:

```text
model/material_model.pkl
model/scaler.pkl
```

### Step 2: Start the Streamlit Application

```bash
streamlit run app.py
```

### Step 3: Open the Application

Streamlit will provide a local address, normally:

```text
http://localhost:8501
```

Open it in your browser.

---

## 🖥️ Application Features

### 1. Prediction Dashboard

Users enter:

- Area
- Number of floors
- Project duration
- Number of workers

The system predicts the required construction materials.

### 2. Material Prediction

The dashboard displays predicted:

- Cement
- Steel
- Bricks
- Asphalt

### 3. Visualizations

The application provides:

- Material prediction bar chart
- Material distribution pie chart
- Prediction history
- Dataset overview

### 4. Delay Risk Indicator

A simple rule-based indicator provides:

- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk

The indicator is based on project duration and number of workers.

> Note: The delay-risk indicator is a rule-based project feature and is separate from the Linear Regression material prediction model.

### 5. Dataset Overview

The application allows users to view sample dataset records and the dataset shape.

---

## 📊 Model Evaluation

The project evaluates the regression model using:

- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **R² Score**

Actual-vs-predicted visualizations can also be used to compare model predictions with test-set values.

---

## 📦 Dataset

The project uses a **synthetic construction dataset** created for machine learning experimentation.

The dataset contains construction project information and material requirement values.

The model specifically uses:

```text
Area_sqft
Building_Floors
Duration_days
Workers
```

to predict:

```text
Cement_bags
Steel_tons
Bricks_units
Asphalt_tons
```

---

## 🎯 Applications

- Construction material planning
- Resource management
- Material requirement estimation
- Project planning
- Construction management support
- Academic machine learning demonstration

---

## 🔮 Future Improvements

Possible future improvements include:

- Using larger real-world construction datasets.
- Comparing Linear Regression with Random Forest and other regression models.
- Improving delay prediction using a dedicated machine learning model.
- Adding more construction project features.
- Deploying the application online.
- Adding user authentication and project history storage.

---

## 👨‍💻 Author

**Uday Shankar Reddy**

B.Tech – Computer Science Engineering (Data Science)

---

## 📄 License

This project is developed for academic and educational purposes.
