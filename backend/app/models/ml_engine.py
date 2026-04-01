import re
import os
import threading
import pickle
from ..core.config import settings

# Global storage for models
transformer_pipeline = None
lr_model = None
rf_model = None

def clean_text(text):
    """Clean text by removing punctuation, links, and special characters."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def train_mock_models():
    """Trains default Logistic Regression and Random Forest mock models if none exist."""
    print("Training new mock models...")
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    
    texts = [
        "The earth is flat and scientists are lying to you.", "Aliens have landed in New York.", "Secret society controls weather.",
        "Eating raw garlic cures all diseases.", "Study shows apples are good for health.", "Stock market up by 2 percent.",
        "President gave a speech on economy.", "Water boils at 100 degrees Celsius.", "NASA launches new rover to Mars."
    ]
    labels = [0,0,0,0,1,1,1,1,1] # 0 = Fake, 1 = Real
    cleaned_texts = [clean_text(t) for t in texts]

    # Model 1: Logistic Regression
    lr = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', LogisticRegression())])
    lr.fit(cleaned_texts, labels)
    with open(settings.LR_MODEL_PATH, "wb") as f: pickle.dump(lr, f)

    # Model 2: Random Forest
    rf = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', RandomForestClassifier())])
    rf.fit(cleaned_texts, labels)
    with open(settings.RF_MODEL_PATH, "wb") as f: pickle.dump(rf, f)
    
    return lr, rf

def ensure_models_loaded():
    """Lazy-load the traditional ML models on-demand using lazy imports for speed."""
    global lr_model, rf_model
    if lr_model is None or rf_model is None:
        if not os.path.exists(settings.LR_MODEL_PATH) or not os.path.exists(settings.RF_MODEL_PATH):
            lr_model, rf_model = train_mock_models()
        else:
            try:
                with open(settings.LR_MODEL_PATH, "rb") as f: lr_model = pickle.load(f)
                with open(settings.RF_MODEL_PATH, "rb") as f: rf_model = pickle.load(f)
            except Exception:
                lr_model, rf_model = train_mock_models()

def predict_text(text, model_type="logistic"):
    """Predict if the text is real or fake using the specified model."""
    if model_type == "transformer":
        global transformer_pipeline
        if transformer_pipeline is None:
             from transformers import pipeline
             try:
                 transformer_pipeline = pipeline("text-classification", model="jy46604790/Fake-News-Bert-Detect")
             except Exception:
                 transformer_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
        
        try:
            truncated_text = text[:1500] 
            result = transformer_pipeline(truncated_text)[0]
            label = result['label'].lower()
            pred_text = "Real News" if label in ['real', 'true', '1', 'label_1', 'positive'] else "Fake News"
            return {"prediction": pred_text, "confidence": round(result['score'] * 100, 2)}
        except Exception as e: return {"prediction": "Unknown", "confidence": 0.0, "error": str(e)}

    # Traditional ML
    cleaned = clean_text(text)
    if not cleaned.strip(): return {"prediction": "Uncertain", "confidence": 0.0}
    
    ensure_models_loaded()
    pipeline = rf_model if model_type == "random_forest" else lr_model
    
    try:
        prediction = pipeline.predict([cleaned])[0]
        probabilities = pipeline.predict_proba([cleaned])[0]
        return {
            "prediction": "Real News" if prediction == 1 else "Fake News",
            "confidence": round(float(max(probabilities)) * 100, 2)
        }
    except Exception as e: return {"prediction": "Unknown", "confidence": 0.0, "error": f"Error: {str(e)}"}
