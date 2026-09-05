import streamlit as st
from resume_parser import extract_resume_text
from agent import screen_resume
import tempfile
import os

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Screening Agent")

st.write(
    "Upload multiple candidate resumes to automatically "
    "evaluate and rank them against the job requirements."
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} resume(s) uploaded successfully.")

    if st.button("🔍 Screen All Resumes"):

        results = []

        for uploaded_file in uploaded_files:

            with st.spinner(f"Analyzing {uploaded_file.name}..."):

                file_extension = os.path.splitext(
                    uploaded_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=file_extension
                ) as temp_file:

                    temp_file.write(uploaded_file.getbuffer())
                    temp_path = temp_file.name

                try:
                    resume_text = extract_resume_text(temp_path)

                    result = screen_resume(resume_text)

                    result["candidate_name"] = uploaded_file.name

                    results.append(result)

                finally:
                    os.remove(temp_path)

        # Sort candidates by match score
        results.sort(
            key=lambda x: x["match_score"],
            reverse=True
        )

        st.subheader("🏆 Candidate Ranking")

        for index, result in enumerate(results, start=1):

            st.markdown(f"### {index}. {result['candidate_name']}")

            st.metric(
                "Match Score",
                f"{result['match_score']}%"
            )

            st.write(
                "Decision:",
                result["decision"]
            )

            st.write(
                "Matched Required Skills:",
                result["matched_required_skills"]
            )

            st.write(
                "Missing Required Skills:",
                result["missing_required_skills"]
            )

            st.write(
                "Candidate Summary:",
                result["candidate_summary"]
            )

            st.divider()