from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-api-key')
def get_api_key():
    api_key = os.getenv('MY_API_KEY')
    return jsonify(api_key=api_key)

if __name__ == "__main__":
    app.run(debug=True)
