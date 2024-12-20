from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ML service is running"}

@app.post("/predict")
def predict(data: dict):
    """
    A dummy prediction endpoint. Replace this logic with your ML model later.
    """
    # Example: Returning the sum of all input values
    prediction = sum(data.values())
    return {"prediction": prediction}
