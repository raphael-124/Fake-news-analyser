from fastapi import APIRouter, HTTPException
from .schemas import TextRequest, UrlRequest, PredictionResponse
from ..services.scraper import scrape_url
from ..models.ml_engine import predict_text

router = APIRouter(prefix="/api")

@router.post("/predict/text", response_model=PredictionResponse)
def predict_from_text(req: TextRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    return predict_text(req.text, req.model_type)

@router.post("/predict/url", response_model=PredictionResponse)
def predict_from_url(req: UrlRequest):
    article_text = scrape_url(req.url)
    result = predict_text(article_text, req.model_type)
    
    # Add preview for UI
    preview_length = 300
    preview = article_text[:preview_length] + ("..." if len(article_text) > preview_length else "")
    result["scraped_text_preview"] = preview
    
    return result
