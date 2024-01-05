from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

# Load environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission and generate story continuation
@app.route('/generate_story', methods=['POST'])
def generate_story():
    prompt = request.form['prompt']
    # Call OpenAI GPT-3 API 
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={
            "prompt": prompt,
            "max_tokens": 200  # Adjust this as needed
        }
    )
    result = response.json()['choices'][0]['text'] if response.status_code == 200 else 'Error generating story'
    return render_template('index.html', prompt=prompt, result=result)

if __name__ == '__main__':
    # app.run(debug=True)
     app.run(host="0.0.0.0", port=8000, debug=True)