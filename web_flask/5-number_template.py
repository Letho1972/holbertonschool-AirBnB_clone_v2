#!/usr/bin/python3

""" Write a script that starts a Flask web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Variable(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python(text="is cool"):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_int(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    return render_template("/5-number.html", n=n)


if __name__ == '__main__':

    """ Run the Flask app on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
