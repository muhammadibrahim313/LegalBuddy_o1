import streamlit as st
import os
import tempfile
from streamlit.components.v1 import html
from file_processor import process_file
from report_generator import generate_report, save_report_as_pdf
from llm_setup import setup_cerebras_client, setup_openai_client, summarize_with_llama, analyze_with_openai
from io import BytesIO

# CSS styles
css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    body {
        font-family: 'Montserrat', sans-serif;
        background-color: #ffffff;
        color: #000000;
    }
    .stApp {
        max-width: 100%;
    }
    h1 {
        font-size: 2.5rem;
        color: #000000;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #000000;
        color: #ffffff;
        border: 2px solid transparent;  /* Added a transparent border */
        padding: 1rem 2rem;  /* Adjusted padding to match 'Get Started Now' style */
        font-size: 1.2rem;    /* Increased font size */
        border-radius: 5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;     /* Added top margin for spacing */
        margin-left: auto;     /* Centered horizontally */
        margin-right: auto;    /* Centered horizontally */
        display: block;        /* Changed to block for centering */
    }
    .stButton > button:hover {
        background-color: #ffffff;  /* Change background to white on hover */
        color: #000000;              /* Change text color to black on hover */
        border: 2px solid #000000;  /* Add black border on hover */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .stFileUploader > div > div {
        background-color: #f8f8f8;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 1rem;
    }
    .stProgress > div > div > div > div {
        background-color: #000000;
    }
    .stMarkdown {
        background-color: #f8f8f8;
        border-radius: 5px;
        padding: 1rem;
        margin-top: 1rem;
    }
    .stDownloadButton > button {
        background-color: #000000;
        color: #ffffff;
        border: 2px solid transparent;  /* Added a transparent border */
        padding: 1rem 2rem;  /* Adjusted padding */
        font-size: 1.2rem;    /* Increased font size */
        border-radius: 5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;     /* Added top margin for spacing */
        margin-left: auto;     /* Centered horizontally */
        margin-right: auto;    /* Centered horizontally */
        display: block;        /* Changed to block for centering */
    }
    .stDownloadButton > button:hover {
        background-color: #ffffff;  /* Change background to white on hover */
        color: #000000;              /* Change text color to black on hover */
        border: 2px solid #000000;  /* Add black border on hover */
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
</style>
"""

def main():
    # Inject custom CSS
    # st.markdown(css, unsafe_allow_html=True)
    
    st.title("Document Liability Analysis")

    if 'report' not in st.session_state:
        st.session_state.report = None
    if 'pdf_buffer' not in st.session_state:
        st.session_state.pdf_buffer = None
    if 'report_generated' not in st.session_state:
        st.session_state.report_generated = False

    # File upload
    uploaded_files = st.file_uploader("Choose files", type=["pdf", "doc", "docx", "jpg", "jpeg", "png", "bmp", "tiff", "heic", "pptx", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        # Add a "Send Files" button
        if st.button("Send Files for Analysis"):
            # Set up LLM clients
            cerebras_client = setup_cerebras_client()
            openai_client = setup_openai_client()

            all_summaries = []

            progress_bar = st.progress(0)
            for i, uploaded_file in enumerate(uploaded_files):
                st.write(f"Processing: {uploaded_file.name}")
                
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name

                try:
                    # Process the file
                    extracted_text = process_file(tmp_file_path)

                    # Summarize with LLaMA
                    summary = summarize_with_llama(cerebras_client, extracted_text)
                    all_summaries.append(f"Summary of {uploaded_file.name}:\n{summary}")

                except Exception as e:
                    st.error(f"An error occurred while processing {uploaded_file.name}: {str(e)}")

                finally:
                    # Clean up the temporary file
                    os.unlink(tmp_file_path)
                
                # Update progress bar
                progress_bar.progress((i + 1) / len(uploaded_files))

            # Analyze all summaries with OpenAI
            if all_summaries:
                st.write("Generating liability analysis...")
                analysis = analyze_with_openai(openai_client, all_summaries)

                # Generate and store report
                st.session_state.report = f"# Liability Analysis Report\n\n{analysis}"
                st.markdown(st.session_state.report)

                # Generate and store PDF
                st.session_state.pdf_buffer = save_report_as_pdf(st.session_state.report)

                # Set the flag to indicate that the report has been generated
                st.session_state.report_generated = True

            st.success("All files processed successfully!")

    # Display the report only if it hasn't been displayed yet
    if st.session_state.report and not st.session_state.report_generated:
        st.markdown(st.session_state.report)
        st.session_state.report_generated = True

    if st.session_state.pdf_buffer:
        st.download_button(
            label="Download Liability Analysis PDF",
            data=st.session_state.pdf_buffer,
            file_name="liability_analysis_report.pdf",
            mime="application/pdf"
        )

    else:
        st.write("Please upload files to analyze.")

if __name__ == "__main__":
    main()
