#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        return render_template('state.html', state=state)
    else:
        return render_template('not_found.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
