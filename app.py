from flask import Flask, request, jsonify
import easyocr

app = Flask(__name__)
reader = easyocr.Reader(['ar', 'en'])

@app.route('/')
def index():
    return 'OCR Server is running!'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    result = reader.readtext(image.stream.read(), detail=0)
    return jsonify({'text': result})

if __name__ == '__main__':
    app.run()
