#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all State objects"""
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def display_cities_by_state(state_id):
    """Display a HTML page with a list of City objects linked to a State"""
    states = storage.all('State').values()
    for state in states:
        if state.id == state_id:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-cities.html', state=state, cities=cities)
    return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
