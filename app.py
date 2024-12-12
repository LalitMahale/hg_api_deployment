from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API on Hugging Face Spaces!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
