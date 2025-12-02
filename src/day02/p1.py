data = open("input.txt").read().split(",")

total = 0
for r in data:
    start, end = r.split("-")
    for i in range(int(start), int(end)):
        num = str(i)
        first_half = num[:len(num)//2]
        second_half = num[len(num)//2:]
        if first_half == second_half:
            total += i

print(total)
