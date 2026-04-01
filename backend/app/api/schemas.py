from pydantic import BaseModel, HttpUrl
from typing import Optional

class TextRequest(BaseModel):
    text: str
    model_type: str = "logistic"

class UrlRequest(BaseModel):
    url: str
    model_type: str = "logistic"

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    scraped_text_preview: Optional[str] = None
    error: Optional[str] = None
