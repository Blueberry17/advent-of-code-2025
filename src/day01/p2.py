data = open("input.txt").read().split()

total = 0
current = 50
for line in data:
    if line[0] == "L":
        mult = -1
    else:
        mult = 1

    for i in range(int(line[1:])):
        current += mult
        current %= 100
        if current == 0:
            total += 1

    print(current, total)

print(total)
