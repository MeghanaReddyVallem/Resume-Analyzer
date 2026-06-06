skills_db = [

    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "flask",
    "mongodb",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "artificial intelligence",
    "tensorflow",
    "pandas",
    "numpy"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:

            found_skills.append(skill)

    return found_skills