import numpy as np


def init_game():
    state = np.array([
        [4, 8, 0, 0, 0, 0, 6, 0, 3],
        [1, 0, 6, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 1, 0],
        [7, 5, 4, 1, 2, 0, 0, 8, 6],
        [0, 3, 0, 9, 5, 0, 0, 0, 0],
        [6, 0, 9, 8, 7, 0, 5, 3, 2],
        [0, 4, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 8, 1, 0, 5],
        [0, 0, 0, 0, 3, 7, 0, 6, 9]
    ])
    assert state.shape == (9, 9), 'Error: game board initialize with incorrect dimension'
    return state


def plot_board(state):
    board = '-------------------------------\n'
    for row in range(9):
        board += '|'
        for col in range(9):
            board += f' {str(state[row, col]) if state[row, col] != 0 else " "} '
            if col in [2, 5, 8]:
                board += '|'
        board += '\n'
        if row in [2, 5, 8]:
            board += '-------------------------------\n'
    print(board)

