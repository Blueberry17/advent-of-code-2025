data = open("input.txt").read().split()

ranges = []

for line in data:
    if "-" not in line:
        break
    a, b = map(int, line.split("-"))
    ranges.append((a, b))

ranges.sort()
merged = []
cur_a, cur_b = ranges[0]

for a, b in ranges[1:]:
    if a <= cur_b + 1:
        cur_b = max(cur_b, b)
    else:
        merged.append((cur_a, cur_b))
        cur_a, cur_b = a, b

merged.append((cur_a, cur_b))

total = sum(b-a+1 for a,b in merged)
print(total)
