data = open("input.txt").read().split()

total = 0
for line in data:
    num = ""
    max_index = -1
    # noinspection PyRedeclaration
    old_max_index = -1
    for i in range(12):
        maximum = float("-inf")
        for index, j in enumerate(line[max_index+1:len(line)-(11-i)]):
            if int(j) > maximum:
                maximum = int(j)
                max_index = old_max_index + index + 1
                if maximum == 9:
                    break
        num += str(maximum)
        old_max_index = max_index
    total += int(num)

print(total)
