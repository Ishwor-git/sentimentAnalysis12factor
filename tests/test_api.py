import pytest
from fastapi.testclient import TestClient
from src.sentimentAnalysis.api import app

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

client = TestClient(app)

def test_predict_sentiment():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "score" in data
    assert data["label"] in ["POSITIVE", "NEGATIVE"]


def test_positive_sentiment():
    response = client.post("/predict", json={"text": "I absolutely love this product!"})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] in ["POSITIVE", "LABEL_1"]
    assert data["score"] > 0.5

def test_negative_sentiment():
    response = client.post("/predict", json={"text": "This is the worst experience I've ever had."})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] in ["NEGATIVE", "LABEL_0"]
    assert data["score"] > 0.5
