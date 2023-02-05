#!/usr/bin/python3
"""Definition of a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    The hello_world function returns the string 'Hello HBNB!'
    :return: The string `Hello HBNB!`
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    The hbnb function returns the string 'HBNB'
    :return: The string `HBNB`
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
