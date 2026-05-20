from flask import Flask, render_template, request, jsonify
from utils.analyzer import analyze_password

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")

    result = analyze_password(password)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
