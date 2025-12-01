def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if line.strip().istitle():
            return line.strip()
    return "Unknown"

def extract_email(text):
    words = text.split()
    for word in words:
        if "@" in word:
            return word
    return "Not found"

def extract_phone(text):
    words = text.split()
    for word in words:
        if word.isdigit() and len(word) >= 10:
            return word
    return "Not found"

def extract_skills(text, skill_set):
    skills_found = []
    for skill in skill_set:
        if skill.lower() in text.lower():
            skills_found.append(skill)
    return skills_found
