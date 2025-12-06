data = open("input.txt").read().split()

ranges = []
for line in data:
    if not "-" in line:
        break
    a, b = line.split("-")
    ranges.append((int(a), int(b)))

total = 0
for item in data:
    if "-" not in item:
        found = False
        for a, b in ranges:
            if a <= int(item) <= b:
                found = True
        if found:
            total += 1
print(total)
