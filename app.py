from flask import Flask, request, jsonify
import easyocr

app = Flask(__name__)
reader = easyocr.Reader(['ar', 'en'])

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    result = reader.readtext(image.read())
    text = ' '.join([item[1] for item in result])
    return jsonify({'text': text})
