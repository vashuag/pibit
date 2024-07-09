from flask import Flask, request, render_template, jsonify
from openai import OpenAI
import os
from PyPDF2 import PdfReader

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)

def read_file(file):
    try:
        return file.read().decode('utf-8')
    except UnicodeDecodeError:
        try:
            return file.read().decode('latin-1')
        except UnicodeDecodeError:
            return None

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    content = None
    if file.filename.lower().endswith('.pdf'):
        content = read_pdf(file)
    else:
        content = read_file(file)

    if content is None:
        return jsonify({"error": "Unable to decode the file content"})

    prompt = (
        "You are an expert in parsing resumes. I am going to give you a resume, and I want you to convert it into a structured JSON format. "
        "Here is the resume content:\n\n"
        f"{content}\n\n"
        "Please parse this content into a JSON format with the following structure: "
        "{ 'Name': '', 'Contact Information': {'Email': '', 'Phone': '', 'Address': ''}, 'Summary': '', 'Work Experience': [], 'Education': [], 'Skills': [], 'Certifications': [], 'Projects': [], 'Publications': [], 'Languages': [] }."
    )

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5
    )
    parsed_content = response.choices[0].text.strip()
    return jsonify({"parsed_content": parsed_content})

if __name__ == '__main__':
    app.run(debug=True)
