data = open("input.txt").read().split()

lines = open("input.txt").read().count("\n")
operands = data[:len(data)//(lines+1)*lines]
operators = data[len(data)//(lines+1)*lines:]

total = 0
length = len(operands)//lines

for i in range(length):
    if operators[i] == "*":
        to_add = 1
        for j in range(lines):
            to_add *= int(operands[i+j*length])
    else:
        to_add = 0
        for j in range(lines):
            to_add += int(operands[i+j*length])
    total += to_add

print(total)
