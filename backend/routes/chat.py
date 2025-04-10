from flask import Blueprint, request, jsonify
from llm.model.llama_utils import chat_with_llama

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("prompt")
    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400

    response = chat_with_llama(user_input)
    return jsonify({"response": response})