from flask import Flask, jsonify
from data_example import Tools
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*') 

@app.route('/')
def index():
    return "Greeting's From the BACKEND"

@app.route('/jet')
def jet():
    response = jsonify(Tools)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)