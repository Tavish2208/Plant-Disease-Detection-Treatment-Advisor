from flask import Flask, render_template
from routes.predict import predict_bp  # Assuming you have the predict blueprint
from routes.chat import chat_bp  # Correctly import the chat blueprint

app = Flask(__name__)

# Register Blueprints for the routes
app.register_blueprint(predict_bp)  # Ensure this is properly defined in `predict.py`
app.register_blueprint(chat_bp)    # Register the chat blueprint

@app.route('/')
def home():
    print("Serving index.html")
    return render_template('index.html')

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error while running the app: {e}")
