# Generative AI-Powered Resume Analyzer

This project demonstrates how to analyze and score resumes using Google Generative AI (Gemini). It includes:
- Real-time extraction of mandatory fields (Name, Contact, University, etc.) from uploaded PDFs.
- AI/ML and Gen AI experience scoring (1–3).
- Real-time comparison against a Job Description (JD) for a "match percentage."
- Batch processing of PDFs from local upload or a Google Drive folder (via Drive API).
- Export of results to Excel.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Demo / Hosted Link](#demo--hosted-link)
- [Screenshots](#screenshots)
- [Notes on Generative AI Usage](#notes-on-generative-ai-usage)
- [Author / Credits](#author--credits)

---

## Features
1. **Generative AI for Advanced Resume Parsing**: Utilizes Gemini from Google.
2. **Interactive UI**: Upload resumes via PDF or Google Drive and view extracted information in real-time on the same screen.
3. **Scoring and Matching**: Scores for AI/ML and Gen AI skills and real-time JD match percentage.
4. **Batch Processing**: Handles up to 100 PDF resumes via local upload or Google Drive.
5. **Export Options**: Detailed extraction results in Excel format.

---

## Requirements
- **Python 3.8+**
- Dependencies as listed in [requirements.txt](requirements.txt), including `streamlit`, `google-generativeai`, and others.
- Google Drive API access for folder processing.

---

## Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/ShantamShukla/AI-Powered-Resume-Analyzer
   cd ResumeAnalyzer
   ```
2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables** in a `.env` file:
   - `GOOGLE_API_KEY`: Your Gemini API key.
   - `GOOGLE_SERVICE_ACCOUNT_INFO`: Your Google service account JSON.

---

## Usage

1. **Launch the app**:
   ```bash
   streamlit run app.py
   ```
2. **Interact with the UI**:
   - Upload PDFs directly or via Google Drive link.
   - Optionally enter a job description for JD match analysis.
3. **View extracted details** and match scores in real-time.
4. **Download results** as Excel files directly from the UI.

---

## Project Structure
```
ResumeAnalyzer/
├─ app.py               # Main Streamlit app
├─ requirements.txt     # Dependencies
├─ .env.example         # Environment variable example
├─ README.md            # Project documentation
└─ ...
```

---

## Demo / Hosted Link
- [Streamlit Cloud Hosted App](https://gen-ai-resume-analyz.streamlit.app/)

---

## Screenshots
(Update with actual screenshots reflecting the new interface)

---

## Notes on Generative AI Usage
- Detailed information on how the Gemini model is utilized for parsing and scoring resumes against job descriptions.

---

## Author / Credits
- **Author**: Shantam Shukla
- **Credits**: Utilizes Google's Generative AI technology and other open-source libraries.

---

**Explore and analyze resumes efficiently and effectively with our AI-powered tool!**