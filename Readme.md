FastAPI ML Model Deployment

This project demonstrates how to deploy a machine learning model using FastAPI, a modern web framework for building APIs with Python 3.7+ based on standard Python type hints. The API allows users to upload CSV files, receive predictions from a trained model, and get model explanations using SHAP (SHapley Additive exPlanations).
Features

    /predict/: Upload a CSV file and get predictions from the machine learning model.
    /explain/: Upload a CSV file and get SHAP explanations for the model's predictions.
    Preprocessing is handled automatically using custom Python scripts.

Project Structure

bash

fastapi_ml_deployments/
│
├── app/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main FastAPI application
│   ├── model.py                 # Model loading and prediction logic
│   ├── preprocess.py            # Data preprocessing functions
│   ├── explain.py               # SHAP explanation logic
│
├── model/                       # Directory containing pre-trained model
│   └── best_model.pkl           # Serialized model file
│
├── data/                        # Sample data files for testing
│   └── sample_input.csv         # Example input data
│
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── .gitignore                   # Files/folders to ignore in git

Getting Started
Prerequisites

    Python 3.8+
    Install conda or pip as your package manager

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/fastapi_ml_deployments.git
cd fastapi_ml_deployments

Create a virtual environment and activate it:

bash

python -m venv myenv
source myenv/bin/activate  # For Linux/macOS
myenv\Scripts\activate     # For Windows

Install dependencies:

---------

    pip install -r requirements.txt

    Ensure that you have the machine learning model file (best_model.pkl) placed in the model/ directory.

Running the Application

    Start the FastAPI server:

--------

uvicorn app.main:app --reload

Go to http://127.0.0.1:8000 in your browser. You should see a welcome message.

You can now use the API to get predictions and explanations. For instance, use tools like Postman or cURL to send requests.

Example request (using cURL):

------

    curl -X 'POST' \
      'http://127.0.0.1:8000/predict/' \
      -H 'accept: application/json' \
      -H 'Content-Type: multipart/form-data' \
      -F 'file=@data/sample_input.csv;type=text/csv'

API Endpoints

    GET /:
        Returns a welcome message.
    POST /predict/:
        Upload a CSV file to get model predictions.
        Input: CSV file (e.g., sample_input.csv)
        Output: JSON response containing predictions.
    POST /explain/:
        Upload a CSV file to get SHAP explanations for the predictions.
        Input: CSV file
        Output: JSON response containing SHAP explanations.

Example Input

The API expects a CSV file where each row contains features for model prediction. An example file might look like this:

-----

age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
63,1,3,145,233,1,0,150,0,2.3,0,0,1
37,1,2,130,250,0,1,187,0,3.5,0,0,2
41,0,1,130,204,0,0,172,0,1.4,2,0,2

-----

SHAP Explanation

The /explain/ endpoint provides a SHAP explanation for each prediction, allowing you to interpret model behavior.
Testing

You can use pytest or any other testing framework to ensure your API functions correctly.
Deployment

To deploy the API, you can use platforms like Heroku, AWS, or Google Cloud. You will need to adapt the deployment process depending on your target environment.
Contributing

Feel free to submit issues or pull requests if you want to improve this project.
License

This project is licensed under the MIT License. See the LICENSE file for more information.

This README outlines the steps necessary to use and deploy the FastAPI-based machine learning model API.