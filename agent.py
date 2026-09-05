import os
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", api_key is not None)

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)


def load_job_requirements():
    with open("job_requirements.json", "r", encoding="utf-8") as file:
        return json.load(file)


def screen_resume(resume_text):

    job = load_job_requirements()

    prompt = f"""
You are an AI Resume Screening Agent.

Analyze the candidate resume against the following job requirements.

JOB REQUIREMENTS:
{json.dumps(job, indent=2)}

CANDIDATE RESUME:
{resume_text}

Evaluate:
1. Required skills
2. Preferred skills
3. Relevant experience
4. Overall suitability

Return ONLY valid JSON in exactly this format:

{{
    "match_score": 0,
    "matched_required_skills": [],
    "missing_required_skills": [],
    "matched_preferred_skills": [],
    "candidate_summary": "",
    "strengths": [],
    "weaknesses": [],
    "decision": "SHORTLIST"
}}

Rules:
- match_score must be between 0 and 100.
- Use SHORTLIST if the candidate is suitable.
- Use REJECT if the candidate is not suitable.
- Do not invent skills or experience that are not present in the resume.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result_text = response.output_text

    try:
        result = json.loads(result_text)
    except json.JSONDecodeError:
        print("AI returned invalid JSON:")
        print(result_text)
        raise

    return result