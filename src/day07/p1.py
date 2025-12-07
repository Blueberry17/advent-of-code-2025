data = open("input.txt").read().split()
grid = []
for line in data:
    new_line = []
    for char in line:
        new_line.append(char)
    grid.append(new_line)

total = 0
changed = True
current = [(data[0].index("S"), 0)]
while changed:
    changed = False
    new = []
    for x, y in current:
        if y+1 < len(grid):
            if grid[y+1][x] == ".":
                grid[y+1][x] = "|"
                new.append((x,y+1))
                changed = True
            elif grid[y+1][x] == "^":
                total += 1
                if x+1 < len(grid[0]):
                    grid[y+1][x+1] = "|"
                    new.append((x+1,y+1))
                    changed = True
                if x-1 >= 0:
                    grid[y+1][x-1] = "|"
                    new.append((x-1,y+1))
                    changed = True
    current = new

print(total)
