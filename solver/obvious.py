import numpy as np


def get_solution(row, col, square):
    in_row = row[np.nonzero(row)]
    in_col = col[np.nonzero(col)]
    in_sq = square[np.nonzero(square)]
    union = np.union1d(in_row, in_col)
    union = np.union1d(union, in_sq)
    if len(union) == 8:
        for solution in range(1, 10):
            if solution not in union:
                return solution
    else:
        return 0


def get_square(i, j, state):
    square_indices = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2],
                      3: [3, 4, 5], 4: [3, 4, 5], 5: [3, 4, 5],
                      6: [6, 7, 8], 7: [6, 7, 8], 8: [6, 7, 8]}
    rows = square_indices[i]
    cols = square_indices[j]
    square = []
    for row in rows:
        for col in cols:
            square.append(state[row, col])
    return np.array(square)


def update(state):
    updates = 0
    for i in range(9):
        for j in range(9):
            if state[i, j] != 0:
                continue
            row = state[i, :]
            col = state[:, j]
            square = get_square(i, j, state)
            solution = get_solution(row, col, square)
            if update != 0:
                state[i, j] = solution
                updates += 1
    return state, updates

