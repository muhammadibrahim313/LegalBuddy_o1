
from streamlit.components.v1 import html


import streamlit as st

# Updated HTML content with full-width layout and black/white theme
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legal Buddy</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
        
        body, html {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow-x: hidden;
        }
        body {
            background-color: #ffffff;
            color: #000000;
            display: flex;
            flex-direction: column;
        }
        .container {
            width: 100%;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        header {
            text-align: center;
            padding: 4rem 0;
            background-color: #f8f8f8;
        }
        h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            color: #000000;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        .subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            color: #333333;
        }
        .cta-button {
            display: inline-block;
            background-color: #000000;
            color: #ffffff;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            text-decoration: none;
            border-radius: 5px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .cta-button:hover {
            background-color: #333333;
            transform: translateY(-3px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        }
        .features {
            display: flex;
            justify-content: space-around;
            padding: 4rem 2rem;
            flex-wrap: wrap;
            background-color: #ffffff;
        }
        .feature {
            flex-basis: calc(33.333% - 2rem);
            padding: 2rem;
            background-color: #f8f8f8;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            margin-bottom: 2rem;
        }
        .feature:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        .feature h2 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: #000000;
        }
        .feature p {
            font-size: 1.1rem;
            color: #333333;
        }
        .feature i {
            font-size: 3rem;
            color: #000000;
            margin-bottom: 1rem;
        }
        @media (max-width: 768px) {
            .feature {
                flex-basis: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Legal Buddy</h1>
            <p class="subtitle">Your intelligent companion for liability analysis and legal document insights.</p>
            <a href="#" class="cta-button">Get Started Now</a>
        </header>
        
        <div class="features">
            <div class="feature">
                <i class="fas fa-file-alt"></i>
                <h2>Smart Document Analysis</h2>
                <p>Upload and analyze various document types for potential liabilities with ease.</p>
            </div>
            <div class="feature">
                <i class="fas fa-brain"></i>
                <h2>AI-Powered Insights</h2>
                <p>Leverage cutting-edge AI models for comprehensive and accurate legal analysis.</p>
            </div>
            <div class="feature">
                <i class="fas fa-chart-bar"></i>
                <h2>Instant Reports</h2>
                <p>Generate and download detailed liability analysis reports in PDF format within seconds.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the HTML in Streamlit
st.set_page_config(page_title="Legal Buddy", layout="wide")
st.components.v1.html(html_content, height=900, scrolling=False)