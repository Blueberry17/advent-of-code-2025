import numpy as np


def fill_space(grid, queue):
    shape = shapes[queue.pop(0)]
    combs = all_shapes(shape)

    possible = False
    for cur in combs:
        for i, y in enumerate(grid):
            for j, x in enumerate(y):
                if x == "." and j < len(y)-2 and i < len(grid)-2:
                    works = True
                    for a in range(3):
                        for b in range(3):
                            if grid[i+a][j+b] == "#" and cur[a][b] == "#":
                                works = False
                    if works:
                        possible = True
                        pos_index = (i, j)
                        pos_shape = cur
                if possible:
                    break
            if possible:
                break
        if possible:
            break

    if possible:
        i, j = pos_index
        for a in range(3):
            for b in range(3):
                if pos_shape[a][b] == "#":
                    grid[i+a][j+b] = str(pos_shape[a][b])

        if len(queue) == 0:
            return True
        else:
            return fill_space(grid, queue)
    return False


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
    grid = [["." for _ in range(int(state[0][1]))] for _ in range(int(state[0][0]))]
    queue = []
    for index, shape in enumerate(state[1]):
        for i in range(shape):
            queue.append(index)

    if fill_space(grid, queue):
        total += 1
print(total)
