import re


def extract_experience(text):

    text = text.lower()

    experience_data = []

    patterns = [

        r'(\d+)\s+years',
        r'(\d+)\s+year',
        r'(\d+)\s+months',
        r'(\d+)\s+month'
    ]

    for pattern in patterns:

        matches = re.findall(pattern, text)

        for match in matches:

            experience_data.append(match)

    if "fresher" in text:

        experience_data.append("fresher")

    return experience_data