import numpy as np
from itertools import islice


input_1 = "input_04.txt"

boards = []

# converting input into 1d and 3d numpy arrays:
with open(input_1, mode="r") as text_file:
    draws = np.array([int(item) for item in text_file.readline().strip("\n").split(",")])
    while text_file.readline():
        boards.append([list(map(int, line.strip().split())) for line in islice(text_file, 0, 5) if line != "\n"])
    boards = np.array(boards)

# creating boards to be reduced and "mask" check_board array of zeroes (False) of same size as boards array:
reduced = boards.copy()
check_board = np.zeros(reduced.shape, dtype=bool)


for num in draws:
    # changing (by multiplying) False to True if number was drawn for every number in check_board
    check_board += (reduced == num)

    if reduced.shape[0] > 1:

        # checking if any row in mask has 5 numbers drawn, getting number of board, deleting board a mask board:
        if (check_board.sum(axis=1) == 5).any():
            board_num = np.where(check_board.sum(axis=1) == 5)[0]
            reduced = np.delete(reduced, board_num, 0)
            check_board = np.delete(check_board, board_num, 0)

        # checking columns, deleting boards
        if (check_board.sum(axis=2) == 5).any():
            board_num = np.where(check_board.sum(axis=2) == 5)[0]
            reduced = np.delete(reduced, board_num, 0)
            check_board = np.delete(check_board, board_num, 0)

    else:
        # continuing loop (drawing numbers) until winning rule is met for the last board, printing score:
        if (check_board.sum(axis=1) == 5).any() or (check_board.sum(axis=2) == 5).any():
            print(reduced[np.invert(check_board)].sum() * num)
            break
