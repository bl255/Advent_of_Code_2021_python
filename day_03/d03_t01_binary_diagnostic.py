import numpy as np

input_1 = "input_03.txt"

with open(input_1, mode="r") as text_file:
    diagnostics = np.array([list(map(int, line.strip())) for line in text_file.readlines()])
    # moves: input transformed into 2D numpy matrix of integers

gamma_str = "".join((diagnostics.sum(axis=0) > diagnostics.shape[0] / 2).astype(int).astype(str))
# if 0 and 1 are the only options, if (sum of column) > (number of rows/2) the most common element is 1

epsilon_str = gamma_str.translate(str.maketrans("01", "10"))
# only 2 options, epsilon is reverse of gamma

print(int(gamma_str, 2) * int(epsilon_str, 2))
