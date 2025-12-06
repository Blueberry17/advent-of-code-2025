import math

data = open("input.txt").read().split("\n")

operators = data[-1].split()
operands = []

start = 0
for i in range(len(data[0])):
    to_add = True
    for line in data[:-1]:
        if line[i] != " ":
            to_add = False
    if to_add:
        column = []
        for line in data[:-1]:
            column.append(line[start:i])
        operands.append(column)
        start = i+1
column = []
for line in data[:-1]:
    column.append(line[start:])
operands.append(column)

total = 0
for index, column in enumerate(operands):
    new_targets = []
    for i in range(max(map(len, list(map(str, column))))):
        new_num = ""
        for j in column:
            if i < len(j) and j[i] != " ":
                new_num += j[i]
        new_targets.append(int(new_num))
    if operators[index] == "+":
        total += sum(new_targets)
    else:
        total += math.prod(new_targets)

print(total)
