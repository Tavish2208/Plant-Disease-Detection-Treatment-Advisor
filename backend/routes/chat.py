from flask import Blueprint, request, jsonify
from llm.model.llama_utils import chat_with_llama

# ✅ Define the blueprint BEFORE using it
chat_bp = Blueprint('chat', __name__)  # <-- this line was missing/too late

@chat_bp.route('/chat', methods=['POST'])
def chat():
    try:
        print("🛬 Received chat request")
        user_input = request.json.get("prompt")
        user_location = request.json.get("location", "an unknown location")
        weather_data = request.json.get("weather", {})  # ✅ Full weather object

        print("📩 Prompt:", user_input)
        print("📍 Location:", user_location)

        if not user_input:
            return jsonify({"error": "No prompt provided"}), 400

        response = chat_with_llama(user_input, user_location, weather_data)
        return jsonify({"response": response})
    except Exception as e:
        print(f"❌ Error in /chat route: {e}")
        return jsonify({"error": f"An internal error occurred: {e}"}), 500
