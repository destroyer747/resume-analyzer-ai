import os
import re
import numpy as np
import pandas as pd
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load English language model for spaCy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    st.error("Please install the English language model: python -m spacy download en_core_web_sm")
    raise

# Set up Streamlit app
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🤖 AI-Powered Resume Analyzer")
st.markdown("Upload your resume and job description to get an AI-powered analysis")

# File upload section
resume_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx", "txt"])
job_description = st.text_area("Paste Job Description Here", height=200)

def extract_text_from_file(file):
    """Extract text from PDF, DOCX, or TXT files"""
    if file.type == "application/pdf":
        reader = PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        text = " ".join([para.text for para in doc.paragraphs])
    else:
        text = str(file.read(), "utf-8")
    return text

def analyze_resume(resume_text):
    """Analyze resume text using NLP"""
    doc = nlp(resume_text)
    
    # Extract entities
    skills = []
    education = []
    experience = []
    organizations = []
    
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)
        elif ent.label_ == "ORG" and "university" in ent.text.lower():
            education.append(ent.text)
        elif ent.label_ == "ORG":
            organizations.append(ent.text)
    
    # Extract experience using regex
    experience_pattern = r"\b(\d{1,2}\+? years?|\d{1,2}\+? yrs?)\b"
    experience_matches = re.findall(experience_pattern, resume_text, re.IGNORECASE)
    
    # Extract education using regex
    education_pattern = r"(Bachelor|Master|Ph\.?D|B\.?S|M\.?S|Diploma).*?(in|of)?.*?([A-Z][a-zA-Z\s]+)"
    education_matches = re.findall(education_pattern, resume_text, re.IGNORECASE)
    
    return {
        "skills": list(set(skills)),
        "education": education_matches,
        "experience": experience_matches,
        "organizations": list(set(organizations)),
        "word_count": len(resume_text.split()),
        "char_count": len(resume_text)
    }

def calculate_compatibility(resume_text, job_desc_text):
    """Calculate compatibility score between resume and job description"""
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_desc_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(similarity * 100, 2)

def visualize_analysis(analysis):
    """Create visualizations for the analysis"""
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    
    # Skills word cloud
    skills_text = " ".join(analysis["skills"])
    wordcloud = WordCloud(width=300, height=200, background_color="white").generate(skills_text)
    ax[0, 0].imshow(wordcloud, interpolation="bilinear")
    ax[0, 0].set_title("Skills Word Cloud")
    ax[0, 0].axis("off")
    
    # Education bar chart
    if analysis["education"]:
        education_df = pd.DataFrame(analysis["education"], columns=["Degree", "Preposition", "Field"])
        education_counts = education_df["Degree"].value_counts()
        education_counts.plot(kind="bar", ax=ax[0, 1])
        ax[0, 1].set_title("Education Breakdown")
    
    # Experience pie chart
    if analysis["experience"]:
        experience_df = pd.DataFrame(analysis["experience"], columns=["Experience"])
        experience_counts = experience_df["Experience"].value_counts()
        experience_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax[1, 0])
        ax[1, 0].set_title("Experience Distribution")
    
    # Organization bar chart
    if analysis["organizations"]:
        org_df = pd.DataFrame(analysis["organizations"], columns=["Organization"])
        org_counts = org_df["Organization"].value_counts().head(5)
        org_counts.plot(kind="barh", ax=ax[1, 1])
        ax[1, 1].set_title("Top Organizations")
    
    plt.tight_layout()
    st.pyplot(fig)

def main():
    if resume_file and job_description:
        with st.spinner("Analyzing your resume..."):
            # Extract text
            resume_text = extract_text_from_file(resume_file)
            
            # Analyze resume
            analysis = analyze_resume(resume_text)
            
            # Calculate compatibility
            compatibility_score = calculate_compatibility(resume_text, job_description)
            
            # Display results
            st.success("Analysis Complete!")
            st.subheader("📊 Resume Analysis Summary")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Compatibility Score", f"{compatibility_score}%")
                st.metric("Total Skills Identified", len(analysis["skills"]))
            
            with col2:
                st.metric("Education Items", len(analysis["education"]))
                st.metric("Experience Items", len(analysis["experience"]))
            
            # Show visualizations
            st.subheader("📈 Visual Analysis")
            visualize_analysis(analysis)
            
            # Show detailed findings
            st.subheader("🔍 Detailed Findings")
            
            with st.expander("Skills Detected"):
                st.write(", ".join(analysis["skills"]))
            
            with st.expander("Education History"):
                for edu in analysis["education"]:
                    st.write(f"- {edu[0]} in {edu[2]}")
            
            with st.expander("Work Experience"):
                for exp in analysis["experience"]:
                    st.write(f"- {exp}")
            
            with st.expander("Organizations Mentioned"):
                st.write(", ".join(analysis["organizations"]))
            
            # Tips for improvement
            if compatibility_score < 70:
                st.subheader("💡 Tips to Improve Your Resume")
                st.write("""
                - Add more keywords from the job description
                - Highlight relevant skills and experience
                - Quantify your achievements with numbers
                - Ensure your resume is well-structured and easy to read
                """)

if __name__ == "__main__":
    main()