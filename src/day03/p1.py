data = open("input.txt").read().split()

total = 0
for line in data:
    maximum = float("-inf")
    last = line[0]
    for num in line[1:]:
        if int(last+num) > maximum:
            maximum = int(last+num)
        if num > last:
            last = num
    total += maximum

print(total)
