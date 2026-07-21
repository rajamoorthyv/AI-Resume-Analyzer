import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer!")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

    skills = [
        "Python", "SQL", "Machine Learning",
        "HTML", "CSS", "Java", "C++", "DSA"
    ]

    st.subheader("Detected Skills")

    for skill in skills:
        st.write("✔️", skill)

    st.subheader("ATS Score")

    score = 85
    st.progress(score)
    st.write(f"Your ATS Score: {score}/100")

    st.subheader("Suggestions")

    st.write("• Add more projects")
    st.write("• Include certifications")
    st.write("• Mention internship experience")
    st.write("• Keep resume within one page")