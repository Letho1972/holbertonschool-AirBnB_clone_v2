#!/usr/bin/python3
"""Web App with Flask"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects in DBStorage."""
    from models.state import State
    from models.city import City
    states = storage.all(State).values()
    cities = storage.all(City).values()

    return render_template("8-cities_by_states.html",
                           cities=cities,
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)