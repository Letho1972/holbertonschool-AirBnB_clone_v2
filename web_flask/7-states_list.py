#!/usr/bin/python3

""" Write a script that starts a Flask web application """

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def afterRequest(self):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """def states_list"""
    from models.state import State
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())

    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':

    """ Run the Flask app on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
