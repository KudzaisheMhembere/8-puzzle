import time
from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/solution')
def get_solutions():
    """
    Generate solution using breatfirst search
    """
    return jsonify(random.sample(range(9), 9))
import time
from flask import Flask, request
from flask.json import jsonify
import random
from api import puzzle

app = Flask(__name__)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/initial')
def get_initial_state():
    """
    Generate solution using breath first search
    """
    print(jsonify(random.sample(range(9), 9)))
    return jsonify(random.sample(range(9), 9))


@app.route('/solution', methods=['POST'])
def get_solution():
    """
    Generate solution using breath first search
    """
    puzzle_board = request.json
    print(puzzle_board)
    puzzle_solution = puzzle.get_solution(puzzle_board)
    print(puzzle_solution)
    return jsonify(puzzle_solution)

