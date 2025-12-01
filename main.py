from parser import extract_name, extract_email, extract_phone, extract_skills
from analyzer import score_candidate

# Sample job description skills
job_skills = ["Python", "SQL", "Excel", "Communication"]

# Load resume text
with open("resumes/sample_resume.txt", "r") as f:
    resume_text = f.read()

# Extract information
name = extract_name(resume_text)
email = extract_email(resume_text)
phone = extract_phone(resume_text)
skills = extract_skills(resume_text, job_skills)

# Score candidate
score = score_candidate(skills, job_skills)

# Display results
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Skills: {', '.join(skills)}")
print(f"Candidate Score for Job: {score}%")
