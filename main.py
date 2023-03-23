import numpy as np
from game.utils import init_game, plot_board
from solver import obvious

state = init_game()

print('Initial state: ')
plot_board(state)

while len(np.nonzero(state)[0]) > 0:
    total_updates = 0
    updates = 1
    while updates > 0:
        state, updates = obvious.update(state)
        total_updates += updates

    print(f'After {total_updates} obvious updates: ')
    plot_board(state)
    move = input('Input move as (row, col, entry) ')
    triplet = [int(move.split(',')[i]) for i in range(3)]
    state[triplet[0], triplet[1]] = triplet[2]

