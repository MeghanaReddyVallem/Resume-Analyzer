📄 Intelligent Resume Analyzer Using NLP and Machine Learning

An AI-powered web application that analyzes resumes, extracts key information, and evaluates candidate suitability based on a job description using NLP techniques.

🚀 Project Overview

This project is a Full Stack Resume Analyzer System that helps automate resume screening. It extracts important details from resumes such as skills, education, and experience, and compares them with a job description to generate an ATS (Applicant Tracking System) score.

✨ Features
📄 Upload Resume (PDF / DOCX)
🧠 Automatic Text Extraction
🔍 Skill Detection using NLP
🎓 Education Extraction
💼 Experience Detection
📊 ATS Score Calculation
🎯 Job Description Matching
⚠️ Missing Skills Identification
🌐 Interactive Web Interface
🏗️ Tech Stack
Frontend
React.js
Axios
HTML, CSS, JavaScript
Backend
Flask (Python)
Flask-CORS
NLP / Processing
pdfplumber (PDF extraction)
python-docx (Word extraction)
Regular Expressions (Regex)
Custom keyword-based NLP logic
📁 Project Structure
ResumeAnalyzer/
│
├── backend/
│   ├── app.py
│   ├── skills.py
│   ├── education.py
│   ├── experience.py
│   ├── parser.py
│   ├── uploads/
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   └── App.js
│   └── package.json
│
└── README.md
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/ResumeAnalyzer.git
cd ResumeAnalyzer
2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
pip install flask flask-cors pdfplumber python-docx
python app.py

Backend runs at:

http://127.0.0.1:5000
3️⃣ Frontend Setup
cd frontend
npm install
npm start

Frontend runs at:

http://localhost:3000
🔥 How It Works
User uploads resume (PDF/DOCX)
Backend extracts text from file
NLP logic detects:
Skills
Education
Experience
User enters job description
System compares resume vs job skills
ATS score is generated
Missing skills are displayed
📊 ATS Score Formula
ATS Score = (Matched Skills / Job Required Skills) × 100
🎯 Example Output
ATS Score: 72%
Missing Skills:
Machine Learning
SQL
TensorFlow
💡 Future Improvements
AI-based skill prediction (ML model)
Resume ranking system
PDF report download
User authentication system
Database integration (MongoDB)
Advanced dashboard with charts
