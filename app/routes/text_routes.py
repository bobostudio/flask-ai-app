from flask import Blueprint, request, jsonify
from app.services.text_service import (
    generate_text,
    analyze_sentiment,
    summarization,
    translate_text,
    answer_question
)

text_bp = Blueprint('text', __name__)

@text_bp.route('/generate',methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    result = generate_text(prompt)
    return jsonify({'result': result})
    
@text_bp.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json.get('text')
    result = analyze_sentiment(text)
    return jsonify({'result': result})

@text_bp.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text')
    result = summarization(text)
    return jsonify({'result': result})


@text_bp.route('/translate',method=['POST'])
def translator():
    text = request.json.get('text')
    return jsonify({'result':  translate_text(text)})

@text_bp.route('/qa', methods=['POST'])
def qa():
    question = request.json.get('question')
    context = request.json.get('context')
    result = answer_question(question, context)
    return jsonify({'result': result})