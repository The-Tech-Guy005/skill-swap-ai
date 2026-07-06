import os
import google.generativeai as genai 
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import markdown
from pypdf import PdfReader
import pdfplumber

app = Flask(__name__)

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data["question"]

    prompt = f"""
    You are an expert ATS and career mentor.

    Analyze this resume:

    {question}

    Return in this format:

    ATS Score: X/100

    1. Current Strengths
    2. Missing Skills
    3. 3-Month Learning Roadmap
    4. Project Ideas
    5. Career Recommendations

    Do NOT repeat the ATS score again in the main response.
    Be consistent with ATS scoring. Give similar scores for similar resumes.
    """

    try:
        response = model.generate_content(prompt)
        answer = markdown.markdown(response.text)

    except Exception:
         answer = """
    <h2>⚠️ Gemini API Error</h2>
    <p>The AI service is temporarily unavailable or the quota has been exceeded.</p>
    <p>Please try again later.</p>
    """

    return jsonify({
        "answer": answer
})

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return jsonify({
        "text": text
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=5001)

