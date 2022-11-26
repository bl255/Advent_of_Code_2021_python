import re
from collections import Counter
import numpy as np

input_1 = "input_05.txt"

positions = []
with open(input_1, mode="r") as text_file:
    for line in text_file:
        positions.append(tuple(int(num) for num in re.split(" -> |,", line.strip())))

all_points = []
for pos in positions:
    if pos[0] == pos[2]:  # horizontal
        all_points += [(pos[0], y) for y in np.linspace(pos[1], pos[3], num=abs(pos[1] - pos[3]) + 1, dtype=int)]
    elif pos[1] == pos[3]:  # vertical
        all_points += [(x, pos[1]) for x in np.linspace(pos[0], pos[2], num=abs(pos[0] - pos[2]) + 1, dtype=int)]
    elif abs(pos[0] - pos[2]) == abs(pos[1] - pos[3]):  # diagonal
        all_points += tuple(zip(np.linspace(pos[0], pos[2], num=abs(pos[0] - pos[2]) + 1, dtype=int),
                                np.linspace(pos[1], pos[3], num=abs(pos[1] - pos[3]) + 1, dtype=int)))

more_than_one = sum(1 for point, value in Counter(all_points).items() if value > 1)
# number of Counter elements which have value > 1

print(more_than_one)
