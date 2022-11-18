input_1 = "input_02.txt"

position = [0, 0]  # [forward, up_and_down]
dict_tr = {"down": 1, "up": -1, "forward": 0}

with open(input_1, mode="r") as text_file:
    moves = ((dict_tr[line.strip().split()[0]], int(line.strip().split()[1])) for line in text_file.readlines())
    # generator object of tuples (type_of_move_from_dict_tr, size_of_move) eg. (0, 6), (0, 6), (-1, 2), (1, 8), (0, 5)

for move in moves:
    if move[0] < 0:
        position[1] -= move[1]
    else:
        position[move[0]] += move[1]


print(position[0] * position[1])
