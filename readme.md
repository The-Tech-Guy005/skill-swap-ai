# 🚀 SkillSwap AI

SkillSwap AI is an AI-powered Resume Analyzer that helps students and job seekers improve their resumes using Google's Gemini AI. It analyzes uploaded resumes, generates an ATS score, identifies missing skills, provides a personalized learning roadmap, recommends projects, and allows users to download a professional PDF report.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 🤖 AI-Powered Resume Analysis using Google Gemini
- 📊 ATS Score Generation
- 💡 Skill Gap Analysis
- 🛣 Personalized Learning Roadmap
- 💼 Career Recommendations
- 🚀 Project Suggestions
- 📑 Professional Multi-page PDF Report
- 🕒 Analysis History Storage
- 🎨 Modern Responsive UI

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask
- Python

### AI
- Google Gemini API

### Libraries
- pdfplumber
- Markdown
- jsPDF
- python-dotenv

---

## 📂 Project Structure

```
skill-swap-ai/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── history.json
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/skill-swap-ai.git
cd skill-swap-ai
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

### 5. Run the Project

```bash
python app.py
```

Open:

```
http://127.0.0.1:5001
```

---

## 📖 How to Use

1. Upload a resume in PDF format.
2. Resume text is automatically extracted.
3. Click **Run Simulated AI Analysis**.
4. View:
   - ATS Score
   - Strengths
   - Missing Skills
   - Learning Roadmap
   - Project Ideas
   - Career Recommendations
5. Download a professional PDF report.
6. Every analysis is saved in `history.json`.

---

## 📄 Generated Report Includes

- ATS Score
- Date & Time
- AI Resume Analysis
- Multi-page Support
- Professional Header
- Footer on Every Page

---

## 📸 Screenshots

> Add screenshots here

- Home Page
- Resume Upload
- AI Analysis
- ATS Score
- PDF Report

---

## 📦 Dependencies

- Flask
- Google Generative AI
- pdfplumber
- Markdown
- jsPDF
- python-dotenv

Install using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- Resume Comparison
- Authentication System
- User Dashboard
- Database Integration
- Resume Templates
- Job Recommendation Engine
- Interview Preparation Module
- AI Chat Assistant

---

## 👥 Contributors

- Hriday Arora
- Abhinav Dixit
- Team Members

---

## 📜 License

This project is developed for educational and hackathon purposes.

---

## ⭐ Acknowledgements

- Google Gemini API
- Flask
- jsPDF
- pdfplumber