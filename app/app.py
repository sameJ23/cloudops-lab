from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CloudOps Lab</h1>
    <p>Service Status: ONLINE</p>
    <p>Running on AWS EC2</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })
