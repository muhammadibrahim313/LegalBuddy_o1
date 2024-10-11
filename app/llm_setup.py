import os
from openai import OpenAI
import streamlit as st
from mongoextract import get_mongodb_data


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
            {"role": "system", "content": "You are a helpful assistant that makes reports or summaries of huge data for a lawyer to save the time of lawyers including the most important part of the data. or data with digits include the important information"},
            {"role": "user", "content": f"Please analyze the following text and make a concise report:\n\n{text}"}
        ],
        max_tokens=2000
    )
    return response.choices[0].message.content

def analyze_with_openai(client, summaries):
    # Step 1: Initial liability analysis
    combined_summaries = "\n\n".join(summaries)
    liability_response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": f"You are an AI assistant that performs liability analysis. Also tell me in percentage who is liable how much. Please perform a liability analysis on the following data and generate a report:\n\n{combined_summaries}"}
        ],
        max_tokens=10000
    )
    liability_report = liability_response.choices[0].message.content
    #print("liability report:",liability_report)

    # Step 2: Legal summarization
    legal_summary_response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": f"You are an expert legal summarizer. Your task is to extract key points and events from legal documents while maintaining brevity and clarity. Focus on the actions, obligations, and outcomes, avoiding mention of specific names, companies, and locations. Please summarize the following liability analysis:\n\n{liability_report}"}
        ],
        max_tokens=1000
    )
    legal_summary = legal_summary_response.choices[0].message.content

    # Step 3: MongoDB search
    mongodb_results = get_mongodb_data(legal_summary)

    # Step 4: Case analysis report
    case_analysis_response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": f"""You are a legal expert tasked with creating a comprehensive case analysis report.
            Here is an example:
            Case Analysis:
            Duty of Care: The business establishment has a duty to ensure the premises are safe for customers. However, as seen in Johnson v. American Standard (S139184), a manufacturer's duty to warn is negated by a plaintiff who has advance knowledge of the product's inherent hazards. In this case, the claimant may have been aware of the potential hazards of the hose, which could negate the business establishment's duty of care.
            Breach of Duty: The claimant alleges that the business establishment breached its duty by failing to properly secure the hose. However, as seen in Hartford Cas. Ins. v. Swift Distrib., Inc. (Docket number: S207172), a claim must specifically allege a breach of duty. In this case, the claimant's allegations are insufficient to establish a breach of duty.
            Causation: The claimant alleges that the tripping incident caused their injuries. However, the presence of pre-existing medical conditions raises concerns about whether the tripping incident was the actual cause of the claimant's injuries.
            Damages: The claimant alleges that they suffered serious injuries as a result of the tripping incident. However, as seen in Hartford Cas. Ins. Co. v. J.R. Marketing, LLC (Docket number: S211645), an insurer must provide a defense to all claims in a third-party complaint if any claims are potentially covered under the policy. In this case, the business establishment may be entitled to reimbursement for defense fees and expenses.
            end of example
            
            {mongodb_results}
            select the CASE Law that are most relevant to my case and tell me how my case law supports my case also include the docket number in the final result
            """}
        ],
        max_tokens=2000
    )
    case_analysis_report = case_analysis_response.choices[0].message.content
    #print("case analysis report:", case_analysis_report)

    # Step 5: Combine reports
    #final_report = f"Liability Analysis Report:\n\n{liability_report}\n\nCase Analysis Report:\n\n{case_analysis_report}"

    formatted_response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "user", "content": f"You are a document formatter.return only the document no introroductory lines.\n\n Here is the liablility report the most important part:\n{liability_report}\n\n Here is the case analysis report the second important part:\n{case_analysis_report}the case analysis will be a heading in the liability report"}
        ],
        max_tokens=5000
    )
    formatted_response = formatted_response.choices[0].message.content
    return formatted_response

# You can then use this function in your Streamlit app
"""def display_analysis(client, summaries):
    st.write("Generating comprehensive legal analysis...")
    final_report = analyze_with_openai(client, summaries)
    st.write(final_report)"""