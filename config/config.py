# config.py
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")  # Replace with your broker's API URL
API_KEY = os.getenv("API_KEY")  # Replace with your API key
IDENTIFIER = os.getenv("IDENTIFIER")  # Replace with your username
PASSWORD = os.getenv("PASSWORD")  # Replace with your password
