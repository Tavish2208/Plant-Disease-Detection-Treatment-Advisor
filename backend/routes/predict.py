from flask import Blueprint, request, jsonify
from models.classifier import predict_disease

predict_bp = Blueprint('predict_bp', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    prediction, treatment = predict_disease(file)
    return jsonify({'prediction': prediction, 'treatment': treatment})