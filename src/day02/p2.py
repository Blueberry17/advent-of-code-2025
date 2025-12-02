data = open("input.txt").read().split(",")


def factors(n):
    factor_list = []
    for i in range(1, n+1):
        if n%i==0:
            factor_list.append(i)
    return factor_list


total = 0
added = set()

for r in data:
    start, end = r.split("-")
    for i in range(int(start), int(end)+1):
        num = str(i)
        splits = factors(len(num))
        for s in splits:
            cut = len(num) // s
            cuts = []
            all_same = True
            for j in range(cut):
                cuts.append(int(num[j*s:(j+1)*s]))
                if j > 0 and cuts[j] != cuts[j-1]:
                    all_same = False
            if all_same and len(cuts) > 1 and i not in added:
                total += i
                added.add(i)

print(total)
