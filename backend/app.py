from flask import Flask, render_template
from routes.predict import predict_bp
from routes.chat import chat_bp

app = Flask(__name__)
app.register_blueprint(predict_bp)
app.register_blueprint(chat_bp)

@app.route('/')
def home():
    print("Serving index.html")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
