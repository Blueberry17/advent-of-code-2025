import numpy as np

def all_shapes(shape):
    rotations = [np.rot90(shape, x) for x in range(4)]
    reflections = [np.flip(x, 1) for x in rotations]
    return rotations + reflections


data = open("input.txt").read().split("\n")

shapes = {}
grids = []
for index, line in enumerate(data):
    if line == "":
        continue
    if line[1] == ":":
        shapes[int(line[0])] = [[data[index + 1][0], data[index + 1][1], data[index + 1][2]],
                                [data[index + 2][0], data[index + 2][1], data[index + 2][2]],
                                [data[index + 3][0], data[index + 3][1], data[index + 3][2]]]
    elif "x" in line:
        parts = line.split()
        size = parts[0][:-1].split("x")
        x, y = int(size[0]), int(size[1])
        grids.append(((x, y), list(map(int, parts[1:]))))

total = 0
for state in grids:
    size = int(state[0][0]) * int(state[0][1])
    constraint_size = 0
    optimised_size = 0
    for shape in range(6):
        shape_size = 0
        op_shape_size = 0
        for row in shapes[shape]:
            shape_size += 3
            op_shape_size += row.count("#")
        constraint_size += shape_size * state[1][shape]
        optimised_size += op_shape_size * state[1][shape]
    if size >= constraint_size:
        total += 1
    else:
        print(size, constraint_size, optimised_size)

print(total)
