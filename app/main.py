from fastapi import FastAPI, UploadFile, File
import pandas as pd
import pickle

app = FastAPI()

# Load the pre-trained model when the app starts
with open("app/best_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict/")
async def get_prediction(file: UploadFile = File(...)):
    # Read the uploaded CSV file with already preprocessed data
    data = pd.read_csv(file.file)

    # Get predictions from the model
    predictions = model.predict(data)
    
    return {"predictions": predictions.tolist()}

@app.post("/explain/")
async def explain_prediction(file: UploadFile = File(...)):
    # Read the uploaded CSV file with preprocessed data
    data = pd.read_csv(file.file)

    # Model prediction probabilities or logic here
    # Add SHAP or any explainability method if needed

    explanation = "SHAP explanation or other explanation logic here."
    
    return {"explanation": explanation}
