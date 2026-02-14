from dotenv import load_dotenv
load_dotenv()

import os
from pathlib import Path

class Config:
    """Application configuration class"""
    
    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    MODEL_NAME = 'models/gemini-2.5-flash'
    
    # Application Settings
    APP_NAME = "AI Chatbot"
    APP_VERSION = "1.0.0"
    
    # Chat Settings
    MAX_HISTORY = 10  # Number of previous messages to include in context
    AUTO_SAVE = True  # Automatically save chat history
    
    # File Paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
    CHAT_HISTORY_DIR = DATA_DIR / 'chat_history'
    
    # Create necessary directories
    DATA_DIR.mkdir(exist_ok=True)
    CHAT_HISTORY_DIR.mkdir(exist_ok=True)
    
    # UI Configuration
    THEME = {
        'primary_color': '#1f77b4',
        'background_color': '#ffffff',
        'secondary_background_color': '#f0f2f6',
        'text_color': '#262730',
    }
    
    # Generation Parameters
    GENERATION_CONFIG = {
        'temperature': 0.7,
        'top_p': 0.8,
        'top_k': 40,
        'max_output_tokens': 2048,
    }
    
    # Safety Settings
    SAFETY_SETTINGS = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]
