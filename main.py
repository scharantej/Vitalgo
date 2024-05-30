
from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Initialize the game board
board = [['.' for _ in range(50)] for _ in range(50)]

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/step', methods=["POST"])
def step():
    data = request.get_json()
    board = data['board']
    # Apply game rules
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
                        if board[x][y] == '#':
                            neighbors += 1
            if board[i][j] == '#' and (neighbors < 2 or neighbors > 3):
                board[i][j] = '.'
            elif board[i][j] == '.' and neighbors == 3:
                board[i][j] = '#'
    return json.dumps({'board': board})

@app.route('/reset', methods=["POST"])
def reset():
    # Reset the game board
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = '.'
    return json.dumps({'board': board})

if __name__ == '__main__':
    app.run(debug=True)
