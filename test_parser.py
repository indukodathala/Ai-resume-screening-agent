from resume_parser import extract_resume_text
from agent import screen_resume


file_path = "resumes/candidate1.pdf.docx"

resume_text = extract_resume_text(file_path)

result = screen_resume(resume_text)

print("\n===== RESUME SCREENING RESULT =====")

print("Match Score:", result["match_score"], "%")

print("\nMatched Required Skills:")
print(result["matched_required_skills"])

print("\nMissing Required Skills:")
print(result["missing_required_skills"])

print("\nMatched Preferred Skills:")
print(result["matched_preferred_skills"])

print("\nFinal Decision:")
print(result["decision"])
print("\nCandidate Summary:")
print(result["candidate_summary"])

print("\nStrengths:")
print(result["strengths"])

print("\nWeaknesses:")
print(result["weaknesses"])

print("===================================")