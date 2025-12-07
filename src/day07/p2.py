data = open("input.txt").read().split()

traversed = []
for i in range(len(data)):
    traversed.append([0] * len(data[0]))
traversed[0][data[0].index("S")] = 1

for y in range(len(data)-1):
    for x in range(len(data[0])):
        if traversed[y][x] == 0:
            continue

        if data[y+1][x] == ".":
            traversed[y+1][x] += traversed[y][x]

        elif data[y+1][x] == "^":
            if x + 1 < len(data[0]):
                traversed[y+1][x+1] += traversed[y][x]
            if x - 1 >= 0:
                traversed[y+1][x-1] += traversed[y][x]

print(sum(traversed[-1]))
