import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/generate_even_numbers/<int:n>', methods=['GET'])
def generate_even_numbers(n):
    if n < 0:
       
