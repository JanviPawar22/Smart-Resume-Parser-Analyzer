def score_candidate(resume_skills, job_skills):
    matched = set(resume_skills).intersection(set(job_skills))
    return round(len(matched)/len(job_skills)*100, 2)
