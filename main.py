import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/generate_even_numbers/<int:n>', methods=['GET'])
def generate_even_numbers(n):
    if n < 0:
        # Indentation inside the if statement
        return jsonify({'error': 'Input should be a non-negative number'})
    else:
        even_numbers = [i for i in range(0, 2 * n, 2)]
        return jsonify({'even_numbers': even_numbers})
