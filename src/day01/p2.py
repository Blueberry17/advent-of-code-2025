data = open("input.txt").read().split()

total = 0
current = 50
for line in data:
    if line[0] == "L":
        mult = -1
    else:
        mult = 1

    to_add = int(line[1:])
    total += to_add // 100
    if current + ((to_add % 100) * mult) >= 100 or current + ((to_add % 100) * mult) <= 0 and current != 0:
        total += 1
    current = (current + to_add * mult) % 100

print(total)
