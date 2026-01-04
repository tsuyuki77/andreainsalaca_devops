from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Di2 - test_image werkt!"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)