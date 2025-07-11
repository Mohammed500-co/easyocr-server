from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ تفعيل CORS مرة واحدة فقط هنا

@app.route('/')
def home():
    return '✅ خادم تحليل الصور يعمل بنجاح!'

@app.route('/analyze_document', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        return jsonify({'error': 'يرجى رفع صورة بصيغة form-data بالمفتاح file'}), 400

    file = request.files['file']
    filename = file.filename.lower()

    try:
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(file.stream)
            extracted_text = pytesseract.image_to_string(image, lang='eng+ara')
            decision = '✅ تم استخراج النص بنجاح' if extracted_text.strip() else '❌ لم يتم العثور على نص واضح'

            return jsonify({
                'extracted_text': extracted_text,
                'decision': decision
            }), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({'error': 'يرجى رفع صورة بصيغة PNG أو JPG فقط'}), 400

    except Exception as e:
        return jsonify({'error': f'حدث خطأ أثناء التحليل: {str(e)}'}), 500
