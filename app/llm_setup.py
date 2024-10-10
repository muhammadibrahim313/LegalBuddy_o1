import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Cerebras (LLaMA 3.1 70B) configuration
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
CEREBRAS_API_BASE = os.getenv("CEREBRAS_API_BASE", "https://run.cerebras.ai/api/v1")
CEREBRAS_MODEL = os.getenv("CEREBRAS_MODEL", "llama-3.1-70b")

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://aimlapi.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "o1-preview")

def setup_cerebras_client():
    return OpenAI(
        api_key=CEREBRAS_API_KEY,
        base_url=CEREBRAS_API_BASE
    )

def setup_openai_client():
    return OpenAI(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_API_BASE
    )

def summarize_with_llama(client, text):
    response = client.chat.completions.create(
        model=CEREBRAS_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def analyze_with_openai(client, summaries):
    combined_summaries = "\n\n".join(summaries)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": f"You are an AI assistant that performs liability analysis on summarized data. Please perform a liability analysis on the following summarized data and generate a report:\n\n{combined_summaries}"}
        ],
        max_tokens=10000
    )
    return response.choices[0].message.content