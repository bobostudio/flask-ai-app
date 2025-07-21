from flask import Blueprint, request, jsonify
from app.services.text_service import (
    generate_text,
)

text_bp = Blueprint('text', __name__)

@text_bp.route('/generate',methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    result = generate_text(prompt)
    # 中文解码

    result_new = result.decode('utf-8')

    return jsonify({'result': result_new}), 200