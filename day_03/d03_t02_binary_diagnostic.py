import numpy as np

input_1 = "input_03.txt"

with open(input_1, mode="r") as text_file:
    diagnostics = np.array([list(map(int, line.strip())) for line in text_file.readlines()])
    # diagnostics: input transformed into 2D numpy matrix of integers


def repeat_rule_filter(input_2d_array, bool_rule):
    reduced_array = input_2d_array.copy()

    rules = {"org_rule": lambda n: reduced_array[:, n] == int(reduced_array[:, n].sum() >= reduced_array.shape[0] / 2),
             # 1 is most common, or 1 if count of 0 and 1 is equal
             "csr_rule": lambda n: reduced_array[:, n] == int(reduced_array[:, n].sum() < reduced_array.shape[0] / 2),
             # 0 is most common, or 0 if count of 0 and 1 is equal
             }

    n = 0
    while reduced_array.shape[0] > 1:
        reduced_array = reduced_array[rules[bool_rule](n)]
        n = (n + 1) % reduced_array.shape[1]
    return "".join((reduced_array[0].astype(str)))


print(int(repeat_rule_filter(diagnostics, "org_rule"), 2) * int(repeat_rule_filter(diagnostics, "csr_rule"), 2))