import os
from openai import OpenAI
import streamlit as st

# Cerebras (LLaMA 3.1 70B) configuration
CEREBRAS_API_KEY = st.secrets["CEREBRAS_API_KEY"]
CEREBRAS_API_BASE = st.secrets["CEREBRAS_API_BASE"]
CEREBRAS_MODEL = st.secrets["CEREBRAS_MODEL"]

# OpenAI configuration
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
OPENAI_API_BASE = st.secrets["OPENAI_API_BASE"]
OPENAI_MODEL = st.secrets["OPENAI_MODEL"]

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