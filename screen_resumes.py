import os
import pymupdf

RESUME_FOLDER = "resume"

def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


# Find all PDF resumes
for filename in os.listdir(RESUME_FOLDER):

    if filename.lower().endswith(".pdf"):

        pdf_path = os.path.join(RESUME_FOLDER, filename)

        print("\n==============================")
        print("Resume:", filename)
        print("==============================")

        resume_text = extract_text_from_pdf(pdf_path)

        print(resume_text[:1000])