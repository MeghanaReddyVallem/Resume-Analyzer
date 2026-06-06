from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from parser import extract_text_from_pdf, extract_text_from_docx
from skills import extract_skills
from education import extract_education
from experience import extract_experience

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return "Resume Analyzer Backend Running Successfully"


@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:
        return {"message": "No file uploaded"}

    file = request.files['resume']

    if file.filename == '':
        return {"message": "No selected file"}

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = ""

    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(filepath)

    elif file.filename.endswith('.docx'):
        text = extract_text_from_docx(filepath)

    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "resume_text": text,
        "skills": skills,
        "education": education,
        "experience": experience
    }


# ================= ATS SCORE API =================

@app.route('/ats', methods=['POST'])
def ats_score():

    data = request.json

    resume_skills = data.get("resume_skills", [])
    job_skills = data.get("job_skills", [])

    job_skills = [skill.strip().lower() for skill in job_skills]

    matched = 0

    for skill in resume_skills:
        if skill in job_skills:
            matched += 1

    score = 0
    if len(job_skills) > 0:
        score = (matched / len(job_skills)) * 100

    missing_skills = list(set(job_skills) - set(resume_skills))

    return jsonify({
        "ats_score": round(score, 2),
        "missing_skills": missing_skills
    })


if __name__ == '__main__':
    app.run(debug=True)