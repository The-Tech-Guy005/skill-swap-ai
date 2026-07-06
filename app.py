import os
import google.generativeai as genai 
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import markdown
from pypdf import PdfReader

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
    You are SkillSwap AI, an expert career mentor.

    Student input:
    {question}

    Provide:

    1. Current strengths
    2. Missing skills
    3. 3-month learning roadmap
    4. 3 project ideas
    5. Career recommendations

    Use headings and bullet points.
    Keep the response concise.
    """

    response = model.generate_content(prompt)
    answer = markdown.markdown(response.text)

    return jsonify({
        "answer": answer
})

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return jsonify({
        "text": text
    })

if __name__ == "__main__":
    app.run(debug=True)

