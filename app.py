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
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)

