import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

UPSTAGE_API_URL = "https://api.upstage.ai/v1/document-ai/ocr"
UPSTAGE_API_KEY = os.getenv("UPSTAGE_API_KEY")

def upstage_ocr(file_path):
    headers = {
        "Authorization": f"Bearer {UPSTAGE_API_KEY}"
    }
    
    with open(file_path, "rb") as file:
        files = {"document": file}
        response = requests.post(UPSTAGE_API_URL, headers=headers, files=files)
    
    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")