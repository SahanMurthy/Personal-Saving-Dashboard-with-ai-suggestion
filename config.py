import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# API keys
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
GEMINI_API_KEY = os.getenv('gen_api')

# Ensure API keys are set
if not ALPHA_VANTAGE_API_KEY or not GEMINI_API_KEY:
    raise ValueError("API keys are not set. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

