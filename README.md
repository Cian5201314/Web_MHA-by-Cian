Overview
A clean, mobile-responsive web application designed to administer and score the DASS-21 (Depression, Anxiety, and Stress Scale). Built with Python and Streamlit, this tool translates a standardized clinical questionnaire into an accessible, user-friendly digital format.

Features
Interactive Questionnaire: Presents the 21 standard statements with an intuitive 0-3 rating scale.

Automated Clinical Scoring: Instantly calculates and multiplies raw scores to match the DASS-42 clinical baseline.

Severity Categorization: Automatically maps user scores to standard clinical thresholds (Normal, Mild, Moderate, Severe, Extremely Severe) for Depression, Anxiety, and Stress.

Mobile-Optimized: Designed to be opened directly via a web link, requiring no app downloads for the end user.

Target Use Cases
Personal mental health tracking and periodic self-reflection.

A lightweight screening utility for IT and data teams managing patient intake at online charity clinics.

A foundational template for integrating standardized clinical assessments into broader telehealth systems.

Tech Stack
Language: Python 3.x

Framework: Streamlit (Handles both backend logic and frontend UI)

Deployment: Streamlit Community Cloud

How to Run Locally
Clone this repository to your local machine.

Install the required dependency:
pip install streamlit

Run the application:
streamlit run web_app.py

Open the provided localhost URL in your web browser.
