# Generative AI-Powered Document Analyzer

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
   git clone https://github.com/ShantamShukla/Information-extraction-using-Gen-AI
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

## Project Overview

In this project, I utilize Google's Generative AI technology, specifically the **Gemini model**, to enhance the functionality of my document analyzer. Below, I detail how the Gemini model is integrated into the system to parse Word documents and provide a nuanced analysis against job descriptions.

### Gemini Model Overview

The Gemini model is part of Google's suite of generative AI tools designed to understand and generate human-like text based on the input provided. In my application, Gemini is leveraged to extract key information from Word documents and to evaluate these details in the context of specific job requirements.

### Parsing Word Documents

The Gemini model processes text extracted from Word documents to identify and categorize essential personal and professional details. This process involves:

- **Extraction of Basic Details**: The model identifies personal information such as the individual’s name, contact details, and address.
- **Educational Background**: Gemini parses the education section to find degrees, universities, graduation dates, and fields of study.
- **Professional Experience**: The model extracts company names, job titles, durations of employment, and descriptions of job responsibilities and achievements.
- **Skills Identification**: Special attention is given to the skills section to catalog both technical and soft skills.

### Job Description Matching

Another critical application of the Gemini model is in matching the parsed document data against a provided job description:

- **Keyword Matching**: The model compares keywords and phrases from the job description with the document to identify overlaps and gaps.
- **Match Percentage Calculation**: It calculates a match percentage that reflects how closely the individual's experiences and skills align with the job requirements.
- **Contextual Analysis**: Beyond simple keyword matching, Gemini understands the context within which terms are used, allowing for a more nuanced match that considers the depth of experience and relevance.

---

This Markdown formatting organizes the information into clear, structured sections with headers and lists, making it easy to read and understand. This format is ideal for incorporating into project documentation or a GitHub README file.

---

## Author / Credits
- **Author**: Shantam Shukla
- **Credits**: Utilizes Google's Generative AI technology and other open-source libraries.

---

**Explore and analyze resumes efficiently and effectively with our AI-powered tool!**