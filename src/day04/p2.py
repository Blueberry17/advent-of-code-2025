def load_grid(path):
    with open(path) as f:
        return [[1 if c == "@" else 0 for c in line.strip()]
                for line in f.read().split()]


def count_neighbors(grid, y, x):
    h, w = len(grid), len(grid[0])
    return sum(grid[y + dy][x + dx] for dy, dx in dirs if 0 <= y + dy < h and 0 <= x + dx < w)


def step(grid):
    new_grid = []
    changes = 0

    for y, row in enumerate(grid):
        new_row = []
        for x, val in enumerate(row):
            if val == 1:
                neighbors = count_neighbors(grid, y, x)
                if neighbors < 4:
                    new_row.append(0)
                    changes += 1
                else:
                    new_row.append(1)
            else:
                new_row.append(0)
        new_grid.append(new_row)

    return new_grid, changes


grid = load_grid("input.txt")
total_changes = 0
dirs = [(0, 1),  (1, 0),  (1, 1),  (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]

while True:
    grid, changes = step(grid)
    if changes == 0:
        break
    total_changes += changes

print(total_changes)
