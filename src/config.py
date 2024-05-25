# config.py
import os
from dotenv import load_dotenv

load_dotenv()

INTEGRATION_TYPE = os.getenv('INTEGRATION_TYPE')
DATABASE_URL = os.getenv('DATABASE_URL')

# Load the OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

CSV_FILE_PATH = os.getenv('CSV_FILE_PATH')
