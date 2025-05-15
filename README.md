# 🧠 Sentiment Analysis API

This project is a **12-factor compliant** sentiment analysis web API built using **FastAPI** and a **pretrained Hugging Face transformer model**. It allows users to predict whether a given piece of text expresses a **positive** or **negative** sentiment.

---

## 🚀 Features

- REST API endpoint (`/predict`) to classify sentiment
- Supports local execution
- Structured using the 12-factor app methodology
- Logging with Loguru

---

## 🧰 Technologies Used

- FastAPI
- Transformers (`pipeline("sentiment-analysis")`)
- Loguru for logging
- Pytest for testing
- Pydantic for settings and validation

---

## ⚙️ Setup & Configuration

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentimentanalysis12factor.git
cd sentimentanalysis12factor
```

### 2. Create a virtual environment and install dependencies
```env
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuration
create a .env file with following setting or Or configure using config.py via Pydantic settings.
```bash
ENVIRONMENT=local
LOG_LEVEL=DEBUG
```

## 🧪 Run Locally
```bash
uvicorn src.sentimentAnalysis.api:app --reload
```
Visit the API docs at: http://localhost:8000/docs

## ✅ Run Tests
```bash
PYTHONPATH=./src pytest
```

## 🧪 Example API Request
**Request  :**
```json
{
  "text": "I love using this API!"
}
```
**Request  :**
```json
{
  "label": "POSITIVE",
  "score": 0.9992
}
```

## 🧑‍💻 Author
Developed by :  Ishwor Raj Pokharel
