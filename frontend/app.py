from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:3000')

@app.route('/')
def index():
    return render_template('index.html', backend_url=BACKEND_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)