"""A basic flask app."""

from flask import Flask, jsonify

APP = Flask(__name__)


@APP.route("/greetings")
def greetings():
    """Return a list of greetings."""
    return jsonify(["Hello, world!", "Hi there!", "Greetings!"])
