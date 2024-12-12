from flask import Flask, jsonify, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API on Hugging Face Spaces!"})

@app.route('/translate')
def translate():
    # Get the 'text' parameter from the query string
    text = request.args.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Perform translation
    translator = GoogleTranslator(source="auto", target="mr")
    result = translator.translate(text)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)

