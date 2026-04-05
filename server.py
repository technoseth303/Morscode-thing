from flask import Flask, request, jsonify
app = Flask(__name__)

@app.post("/run")
def run():
    data = request.json
    text = data.get("text", "")
    return jsonify({"result": text[::-1]})  # example: reverse text

@app.get("/")
def home():
    return "Python backend is running!"
