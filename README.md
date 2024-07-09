# pibit

# Resume Parser Web App

This web application allows users to upload a resume, which is then parsed into JSON format using ChatGPT.

## Setup

Instructions to Run the Project
1. Clone the repository:

git clone https://github.com/vashuag/pibit.git

 cd resume-parser-app

2. Create and activate a virtual environment:
   
python -m venv venv
source venv/bin/activate  
On Windows use `venv\Scripts\activate`

3. Install the dependencies:

pip install -r requirements.txt

4. Set up your OpenAI API key:

export OPENAI_API_KEY='your-openai-api-key'  
On Windows use `set OPENAI_API_KEY=your-openai-api-key`

5. Run the application:

python app.py

6. Open your browser and navigate to
 http://127.0.0.1:5000.
