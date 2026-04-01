import os

class Settings:
    PROJECT_NAME: str = "Fake News Detection API"
    PROJECT_VERSION: str = "1.0.0"
    
    # CORS Configuration
    CORS_ORIGINS: list = ["*"] # Consider restricting to frontend URL in production
    
    # Model Paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR: str = os.path.join(os.path.dirname(BASE_DIR), "data")
    
    LR_MODEL_PATH: str = os.path.join(DATA_DIR, "fake_news_lr_model.pkl")
    RF_MODEL_PATH: str = os.path.join(DATA_DIR, "fake_news_rf_model.pkl")
    HF_MODELS_PATH: str = os.path.join(DATA_DIR, "hf_models.txt")

settings = Settings()
