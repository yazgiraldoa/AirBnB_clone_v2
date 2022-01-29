#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Function that returns C + input text"""
    output = text.replace('_', ' ')
    return "C {}".format(output)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Function that returns Python + input text"""
    output = text.replace('_', ' ')
    return "Python {}".format(output)


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_number(n):
    """Function that returns a number only if it's an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
