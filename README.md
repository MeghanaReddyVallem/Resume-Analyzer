# 📄 Intelligent Resume Analyzer Using NLP and Machine Learning

An AI-powered web application that analyzes resumes, extracts key information, and evaluates candidate suitability based on a job description using NLP techniques.

---

## 🚀 Project Overview

This project is a **Full Stack Resume Analyzer System** that helps automate resume screening.

It extracts important details such as:
- Skills
- Education
- Experience

It compares them with a job description and generates an **ATS (Applicant Tracking System) score**.

---

## ✨ Features

- 📄 Upload Resume (PDF / DOCX)
- 🧠 Automatic Text Extraction
- 🔍 Skill Detection using NLP
- 🎓 Education Extraction
- 💼 Experience Detection
- 📊 ATS Score Calculation
- 🎯 Job Description Matching
- ⚠️ Missing Skills Identification
- 🌐 Interactive Web Interface

---

## 🏗️ Tech Stack

### Frontend
- React.js
- Axios
- HTML, CSS, JavaScript

### Backend
- Flask (Python)
- Flask-CORS

### NLP / Processing
- pdfplumber
- python-docx
- Regular Expressions (Regex)
- Custom NLP logic

---

## 📁 Project Structure

```text
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
```
⚙️ Installation & Setup

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/MeghanaReddyVallem/ResumeAnalyzer.git
cd ResumeAnalyzer

2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install flask flask-cors pdfplumber python-docx
python app.py

📍 Backend runs at:
http://127.0.0.1:5000

3️⃣ Frontend Setup
http://localhost:3000

🔥 How It Works
User uploads a resume (PDF/DOCX)
Backend extracts text using NLP preprocessing
System detects:
Skills
Education
Experience
User provides job description
Resume is compared with job requirements
ATS score is generated
Missing skills are displayed

📊 ATS Score Formula

ATS Score = (Matched Skills / Required Skills) × 100

🎯 Example Output
ATS Score: 72%
Missing Skills:
Machine Learning
SQL
TensorFlow

💡 Future Improvements
🤖 AI-based skill prediction using ML models
📄 Resume ranking system
📊 Advanced analytics dashboard
🔐 User authentication system
🗄️ MongoDB database integration
📥 PDF report download feature

📌 Key Highlights
Fully automated resume screening system
NLP-based information extraction
ATS-style scoring system
Web-based interactive UI

⭐ If you like this project
Give it a ⭐ on GitHub and feel free to improve it further!
