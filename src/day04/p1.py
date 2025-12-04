data = open("input.txt").read().split()

grid = []
for line in data:
    new_line = []
    for index, char in enumerate(line):
        if char == "@":
            new_line.append(1)
        else:
            new_line.append(0)
    grid.append(new_line)

results = 0
for y_index, line in enumerate(grid):
    for x_index, char in enumerate(line):
        if char == 1:
            total = 0
            dirs = [(0,1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1),(-1,0),(0,-1)]
            for direction in dirs:
                if 0 <= (y_index + direction[0]) < len(grid) and 0 <= (x_index + direction[1]) < len(grid[0]):
                    total += grid[y_index + direction[0]][x_index + direction[1]]
            if total < 4:
                results += 1

print(results)
