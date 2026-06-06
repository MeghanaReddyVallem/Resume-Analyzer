education_keywords = [

    "b.tech",
    "m.tech",
    "bachelor",
    "master",
    "computer science",
    "intermediate",
    "ssc",
    "degree",
    "engineering"
]


def extract_education(text):

    text = text.lower()

    found_education = []

    for edu in education_keywords:

        if edu in text:

            found_education.append(edu)

    return found_education