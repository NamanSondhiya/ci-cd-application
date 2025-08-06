from flask import Flask, jsonify
from data_example import Tools
from flask_cors import CORS

print(f"Tools imported: {Tools}")
print(f"Tools type: {type(Tools)}")

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/')
def index():
    return "hello from backend"

@app.route('/jet')
def jet():
    print(f"In jet route, Tools = {Tools}")
    if Tools is None:
        return jsonify({"error": "Tools is None"})
    try:
        result = jsonify(Tools)
        print(f"jsonify result: {result}")
        return result
    except Exception as e:
        print(f"Error in jet route: {e}")
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)