import re
from collections import Counter

input_1 = "input_05.txt"

positions = []
with open(input_1, mode="r") as text_file:
    for line in text_file:
        positions.append(tuple(int(num) for num in re.split(" -> |,", line.strip())))


all_points = []  # all point positions if x1, x2 or y1, y2 pair is identical
for pos in positions:
    if pos[0] == pos[2]:
        all_points += ([(pos[0], y) for y in range(sorted([pos[1], pos[3]])[0], sorted([pos[1], pos[3]])[1] + 1)])
    elif pos[1] == pos[3]:
        all_points += ([(x, pos[1]) for x in range(sorted([pos[0], pos[2]])[0], sorted([pos[0], pos[2]])[1] + 1)])


more_than_one = sum(1 for point, value in Counter(all_points).items() if value > 1)
# sum of Counter elements which have value > 1

print(more_than_one)
