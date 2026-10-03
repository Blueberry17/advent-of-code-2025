import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

data = open("input.txt").read().split("\n")


def solve(required_ints, toggles):
    matrix = [[] for _ in range(len(required_ints))]
    for button in toggles:
        button = list(map(int, button.replace("(","").replace(")","").split(",")))
        for num in range(len(matrix)):
            if num in button:
                matrix[num].append(1)
            else:
                matrix[num].append(0)
    buttons = len(matrix[0])
    result = milp(c=np.ones(buttons), integrality=np.ones(buttons), bounds=Bounds(0, np.inf),
                  constraints=LinearConstraint(np.array(matrix), required_ints, required_ints))
    return round(result.fun)


total = 0
for line in data:
    split_line = line.split()
    toggles = split_line[1:-1]
    required = split_line[-1]
    required_ints = []
    for i in required.replace("{", "").replace("}", "").split(","):
        required_ints.append(int(i))
    total += solve(required_ints, toggles)
print(total)
