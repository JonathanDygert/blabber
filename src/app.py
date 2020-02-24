from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/greetings")
def greetings():
    return jsonify(["Hello, world!", "Hi there!", "Greetings!"])
