import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import pandas as pd
from typing import Dict
import io
import re
import requests
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_drive_service():
    """Create and return a Google Drive API service object"""
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    creds = service_account.Credentials.from_service_account_info(
        json.loads(os.getenv("GOOGLE_SERVICE_ACCOUNT_INFO")), scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    return service

def extract_file_id(link: str) -> str:
    """Extract file ID from Google Drive link"""
    patterns = [
        r'file/d/([a-zA-Z0-9-_]+)',
        r'id=([a-zA-Z0-9-_]+)',
        r'open\?id=([a-zA-Z0-9-_]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, link)
        if match:
            return match.group(1)
    return ""

def download_file_from_drive(file_id: str) -> io.BytesIO:
    """Download file from Google Drive"""
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    file.seek(0)
    return file

def extract_details_from_text(text: str) -> Dict:
    """Extract specific details using Gemini API"""
    extraction_prompt = """
    Extract the following information from the resume text. Return ONLY a valid JSON object with these exact keys:
    {
        "name": "Full name of the person",
        "phone": "Phone number (if multiple, pick primary)",
        "email": "Email address",
        "address": "Full address if available",
        "education": "Most recent education details",
        "skills": "Key technical skills (comma-separated)",
        "experience": "Most recent work experience"
    }
    
    If any field is not found, use "Not found" as the value.
    Ensure the output is valid JSON format.
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"{extraction_prompt}\n\nText to analyze:\n{text}")
        
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:-3]
        
        parsed_data = json.loads(response_text)
        return parsed_data
    except Exception as e:
        st.error(f"Error in extraction: {str(e)}")
        return {
            "name": "Not found",
            "phone": "Not found",
            "email": "Not found",
            "address": "Not found",
            "education": "Not found",
            "skills": "Not found",
            "experience": "Not found"
        }

def read_pdf(file) -> str:
    """Extract text from PDF file."""
    try:
        reader = pdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += str(page.extract_text())
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

def calculate_match(resume_text: str, job_desc: str) -> int:
    """
    A simple example to calculate match percentage based on keyword overlap.
    This is a placeholder function. Implement a real matching algorithm as needed.
    """
    from collections import Counter
    resume_words = Counter(resume_text.split())
    job_desc_words = Counter(job_desc.split())
    common = resume_words & job_desc_words
    total_common = sum(common.values())
    total_words = sum(job_desc_words.values())
    return int((total_common / total_words) * 100) if total_words else 0
    
def main():
    st.set_page_config(page_title="PDF Information Extractor", layout="wide")
    
    # Custom CSS for better form styling
    st.markdown("""
        <style>
        .stTextInput > label {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .stTextArea > label {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .main > div {
            padding: 2em;
            border-radius: 10px;
            background-color: #f8f9fa;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 24px;
            background-color: #black;
            border-radius: 5px;
        }
        .extracted-info {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Create two columns with 1:3 ratio
    col1, col2 = st.columns([2, 4])

    # Left column for file upload options (narrower)
    with col1:
        st.title("📤 Upload")
        st.markdown("---")
        
        tab1, tab2 = st.tabs(["PDF", "Drive"])

        with tab1:
            uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
            job_description_pdf = st.text_area("Job Description (optional)", 
                                         placeholder="Paste job description here...",
                                         height=100,
                                         key="jd_pdf")
            submit_button_pdf = st.button("Submit for Analysis", 
                                        use_container_width=True,
                                        key="submit_pdf")

            if submit_button_pdf and uploaded_file:
                with st.spinner("Reading PDF and extracting information..."):
                    text = read_pdf(uploaded_file)
                    if text:
                        details = extract_details_from_text(text)
                        st.session_state['extracted_details'] = details
                        if job_description_pdf:
                            match_percentage = calculate_match(text, job_description_pdf)
                            st.session_state['match_percentage'] = match_percentage
                        st.success("✅ Extraction successful!")
                    else:
                        st.error("❌ Could not extract text")
        
        with tab2:
            st.markdown("""
            ### Quick Guide:
            1. Upload to Drive
            2. Share → Anyone with link
            3. Copy link below
            """)
            drive_link = st.text_input("Drive PDF link")
            job_description_drive = st.text_area("Job Description (optional)", 
                                               placeholder="Paste job description here...",
                                               height=100,
                                               key="jd_drive")
            submit_button_drive = st.button("Submit for Analysis", 
                                          use_container_width=True,
                                          key="submit_drive")
            
            if submit_button_drive and drive_link:
                try:
                    with st.spinner("Downloading from Drive..."):
                        file_id = extract_file_id(drive_link)
                        if not file_id:
                            st.error("Invalid Drive link")
                            return
                        
                        pdf_file = download_file_from_drive(file_id)
                        text = read_pdf(pdf_file)
                        
                        if text:
                            details = extract_details_from_text(text)
                            st.session_state['extracted_details'] = details
                            if job_description_drive:
                                match_percentage = calculate_match(text, job_description_drive)
                                st.session_state['match_percentage'] = match_percentage
                            st.success("✅ Extraction successful!")
                        else:
                            st.error("❌ Could not extract text")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Right column for extracted information
    with col2:
        st.title("📝 Extracted Information")
        st.markdown("---")
        
        if 'extracted_details' in st.session_state:
            details = st.session_state['extracted_details']
            if 'match_percentage' in st.session_state:
                st.metric("Resume Match with Job Description", 
                         f"{st.session_state['match_percentage']}%")
            
            # Create editable fields with extracted information
            edited_details = {}
            
            edited_details['name'] = st.text_input("Full Name", 
                value=details.get('name', ''),
                placeholder="Full Name")
            
            edited_details['phone'] = st.text_input("Phone Number", 
                value=details.get('phone', ''),
                placeholder="Phone Number")
            
            edited_details['email'] = st.text_input("Email Address", 
                value=details.get('email', ''),
                placeholder="Email Address")
            
            edited_details['address'] = st.text_area("Address", 
                value=details.get('address', ''),
                placeholder="Address",
                height=100)
            
            edited_details['education'] = st.text_area("Education", 
                value=details.get('education', ''),
                placeholder="Education Details",
                height=100)
            
            edited_details['skills'] = st.text_area("Skills", 
                value=details.get('skills', ''),
                placeholder="Technical Skills",
                height=100)
            
            edited_details['experience'] = st.text_area("Experience", 
                value=details.get('experience', ''),
                placeholder="Work Experience",
                height=150)

            # Export button
            if st.button("Export Details"):
                df = pd.DataFrame([edited_details])
                
                # Convert to Excel
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                
                # Offer download
                st.download_button(
                    label="📥 Download as Excel",
                    data=output.getvalue(),
                    file_name="extracted_details.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.info("👈 Upload a PDF or provide a Google Drive link to extract information")
    
if __name__ == "__main__":
    main()