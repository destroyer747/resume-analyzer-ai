# 📄 resume-analyzer-ai

**AI-Powered Resume Analyzer with NLP and Compatibility Scoring**  
An intelligent Python-based application that extracts, analyzes, and compares resume content against job descriptions using **spaCy**, **TF-IDF**, and **cosine similarity**. This tool automates resume screening and provides insights on skills, education, experience, and overall job match percentage.

## 🚀 Features

- 🧠 NLP-based resume analysis using `spaCy`
- 📄 Supports **PDF**, **DOCX**, and **TXT** file formats
- 📊 Extracts and summarizes:
  - Skills
  - Education background
  - Work experience
  - Organizations and job titles
- 💡 Calculates **job-resume compatibility score** using `TfidfVectorizer` + `cosine_similarity`
- 🗃️ Built-in skill database and pattern-based extraction
- 🖥️ CLI-based interaction for real-time analysis
- 📌 Personalized feedback and suggestions based on match score

## 🧠 Technologies Used

| Tech / Lib       | Purpose                          |
|------------------|----------------------------------|
| Python 3.x       | Core programming language        |
| spaCy            | NLP and named entity recognition |
| PyPDF2           | Extract text from PDF resumes    |
| python-docx      | Read `.docx` resumes             |
| scikit-learn     | TF-IDF + Cosine Similarity       |
| re (regex)       | Pattern-based info extraction    |

## 📂 Project Structure

resume-analyzer-ai/
│
├── main.py                      # Entry point script
├── resume\_analyzer.py           # ResumeAnalyzer class
├── sample\_resume.pdf            # Sample resume (optional)
├── requirements.txt             # All dependencies
└── README.md                    # You're here!

> ☑️ *If you're using this in a modular format, split `ResumeAnalyzer` into its own file `resume_analyzer.py`.*

## 🔧 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/destroyer747/resume-analyzer-ai.git
cd resume-analyzer-ai
````

2. **Install Required Libraries**

```bash
pip install -r requirements.txt
```

3. **Download spaCy Language Model**

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Use

1. Run the application:

```bash
python main.py
```

2. Follow the prompts:

   * Upload a resume (`.pdf`, `.docx`, `.txt`)
   * Paste the job description (press Enter **twice** to finish)

3. View the analysis:

   **Extracted skills, education, experience**
   **Resume word/character count**
   **Job Compatibility Score**
   **Smart suggestions to improve your match!**

## 📊 Sample Output

=== RESUME ANALYSIS RESULTS ===

📊 Skills Identified (6):
python, sql, machine learning, leadership, communication, data analysis

🎓 Education History (2):
- Bachelor Of Computer Science
- M.Sc In Artificial Intelligence

💼 Work Experience (2):
- 3+ Years Experience In Data Science
- Worked At ABC Technologies

🏢 Organizations Mentioned (3):
Google, Microsoft, ABC Technologies

📝 Resume Statistics:
- Word Count: 729
- Character Count: 4612

⭐ Job Compatibility Score: 83.47%
💡 Suggestions: Excellent match for this position!

## 📌 To-Do / Future Enhancements

* [ ] Web-based frontend (Streamlit or Flask)
* [ ] Resume ranking for bulk job applications
* [ ] Dynamic skill database loading
* [ ] Visual analytics dashboard

## 🧑‍💼 About the Author

**Abdul Ahad Khan**
AI Enthusiast | Aspiring Machine Learning Engineer
🔗 [GitHub](https://github.com/destroyer747)
📧 Reach out on [LinkedIn](https://www.linkedin.com/in/your-profile) *(replace with actual)*


## 🛡️ License

This project is licensed under the **MIT License**. Feel free to use and build upon it with credit.

## 🌟 Support

If you find this project useful, **consider starring it ⭐ on GitHub** or [sharing it](https://github.com/destroyer747/resume-analyzer-ai) with others.

> *Empower your job applications with AI!*

##✅ Also include a `requirements.txt` file:

txt
spacy
scikit-learn
PyPDF2
python-docx

