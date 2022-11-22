import numpy as np
from itertools import islice

input_1 = "input_04.txt"

boards = []
with open(input_1, mode="r") as text_file:
    draws = np.array([int(item) for item in text_file.readline().strip("\n").split(",")])
    while text_file.readline():
        boards.append([list(map(int, line.strip().split())) for line in islice(text_file, 0, 5) if line != "\n"])
    boards = np.array(boards)


check_board = np.zeros(boards.shape, dtype=bool)
for num in draws:
    check_board += (boards == num)
    if (check_board.sum(axis=1) == 5).any():
        board_num = np.where(check_board.sum(axis=1) == 5)[0]
        print(boards[board_num][np.invert(check_board[board_num])].sum() * num)
        break
    if (check_board.sum(axis=2) == 5).any():
        board_num = np.where(check_board.sum(axis=2) == 5)[0]
        print(boards[board_num][np.invert(check_board[board_num])].sum() * num)
        break
