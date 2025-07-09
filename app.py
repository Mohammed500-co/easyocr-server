from flask import Flask, request, jsonify
import easyocr
import os

app = Flask(__name__)
reader = easyocr.Reader(['ar', 'en'], gpu=False)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    image = request.files['image']
    image_path = os.path.join('temp', image.filename)
    os.makedirs('temp', exist_ok=True)
    image.save(image_path)

    try:
        result = reader.readtext(image_path, detail=0)
        return jsonify({'text': result})
    finally:
        os.remove(image_path)

@app.route('/')
def home():
    return 'OCR Server is Live'
