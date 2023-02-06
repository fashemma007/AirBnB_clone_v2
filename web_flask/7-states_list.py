#!/usr/bin/python3
"""Flask Web App that returns list of states"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Get all state info from database
    Returns: rendered html
    """
    state_dict = (storage.all(State)).values()
    return render_template("7-states_list.html", state_dict=state_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
