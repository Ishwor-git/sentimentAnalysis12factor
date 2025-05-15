from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
from sentimentanalysis12factor.config import settings
from loguru import logger

app = FastAPI()

# Configure logger level from settings
logger.remove()  # Remove default logger
logger.add(
    sink=lambda msg: print(msg, end=""),  # print to stdout
    level=settings.log_level.upper()
)

# Load the pretrained model using config
sentiment_pipeline = pipeline("sentiment-analysis", model=settings.model_name)

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(input: TextInput, request: Request):
    logger.info(f"Received prediction request: {input.text}")
    try:
        result = sentiment_pipeline(input.text)[0]
        logger.info(f"Prediction result: {result}")
        return {"label": result["label"], "score": result["score"]}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return {"error": "Prediction failed"}
