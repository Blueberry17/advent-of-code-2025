data = open("input.txt").read().split()

total = 0
current = 50
for line in data:
    if line[0] == "L":
        current += int(line[1:])
    else:
        current -= int(line[1:])
    current %= 100
    if current == 0:
        total += 1

print(total)
