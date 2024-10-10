import streamlit as st

# Set up the page configuration to wide layout without scrolling
st.set_page_config(page_title="Legal Buddy", layout="wide")

# Initialize session state
if 'show_main' not in st.session_state:
    st.session_state.show_main = False

def show_main_page():
    st.session_state.show_main = True

if st.session_state.show_main:
    # Import and run the main.py content
    from main import main
    main()
else:
    # Landing page content with markdown
    st.markdown("""
        <style>
            /* Remove any margin from the body to prevent unnecessary scrollbars */
          .main {
                padding: 0!important;
                margin: 0!important;
            }
          .block-container {
                padding: 0!important;
            }
            footer {
                background-color: #f8f8f8;
                text-align: center;
                padding-top: 20px;
                margin-bottom: 0!important;
                padding-bottom: 0!important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header section
    st.markdown("""
    <div style='background-color:#f8f8f8; padding: 60px 0; text-align:center;'>
        <h1 style='font-size: 4rem; color:#000000; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Legal Buddy</h1>
        <p style='font-size: 1.5rem; color:#333;'>Your intelligent companion for liability analysis and legal document insights.</p>
    </div>
    """, unsafe_allow_html=True)

    # Get Started button
    if st.button('Get Started Now', on_click=show_main_page):
        st.experimental_rerun()

    # Get Started button styling
    st.markdown("""
        <style>
      .stButton > button {
                background-color: #000;
                color: #fff;
                padding: 1rem 2rem;
                text-decoration: none;
                margin-left: 44%;
                margin-top: 20px;
                border-radius: 5px;
                font-size: 1.2rem;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <div style='display: flex; justify-content: space-around; padding: 10px 10px; flex-wrap: wrap; background-color:#ffffff;'>
            <div style='flex-basis: calc(33.333% - 2rem); background-color:#f8f8f8; padding: 1rem; text-align:center; border-radius:10px; margin-bottom:20px;'>
                <i class="fa fa-gavel"  style='font-size: 2.5rem; color: #000; padding-top: 8px;'></i>
                <h2 style='font-size: 1.8rem; color:#000;'>Liability</h2>
                <p style='font-size: 1.1rem; color:#333;'>This application is designed to analyze documents and generate comprehensive liability reports, ensuring users are well-informed about potential risks and compliance issues.</p>
            </div>
            <div style='flex-basis: calc(33.333% - 2rem); background-color:#f8f8f8; padding: 1rem; text-align:center; border-radius:10px; margin-bottom:20px;'>
                <i class="fas fa-file-alt" style='font-size: 2.5rem; color: #000; padding-top: 8px;'></i>
                <h2 style='font-size: 1.8rem; color:#000;'>Support Files</h2>
                <p style='font-size: 1.1rem; color:#333;'>The app supports multiple file formats, including PDF, XLSX, and DOC, DOCX, etc facilitating seamless document analysis and versatility in use.</p>
            </div>
            <div style='flex-basis: calc(33.333% - 2rem); background-color:#f8f8f8; padding: 1rem; text-align:center; border-radius:10px; margin-bottom:20px;'>
                <i class="fas fa-download" style='font-size: 2.5rem; color: #000; padding-top: 8px;'></i>
                <h2 style='font-size: 1.8rem; color:#000;'>Download Files</h2>
                <p style='font-size: 1.1rem; color:#333;'>Easily download your generated reports in PDF format, crafted using advanced AI models for precise and actionable insights.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)



    # Footer section
    st.markdown("""
    
<footer style='background-color: #f8f8f8; text-align: center; padding-top: 10px;'>
        <p style='font-size: 1rem; color: #666;'>2024 Legal Buddy Team. All Rights Reserved. Developed by Legal Experts and AI Enthusiasts.</p>
    </footer>


    """, unsafe_allow_html=True)
