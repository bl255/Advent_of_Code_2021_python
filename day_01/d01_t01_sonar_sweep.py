input_1 = "input_01.txt"

with open(input_1, mode="r") as text_file:
    depth_list = [int(line.strip()) for line in text_file.readlines()]

decreased = sum((depth_list[num] < depth_list[num + 1] for num, item in enumerate(depth_list[:-1])))

print(decreased)
