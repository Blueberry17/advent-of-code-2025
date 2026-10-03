data = open("input.txt").read().split("\n")


def collapse(x):
    s = ""
    for i in x:
        s += i
    return s


def bfs(node, toggles, required):
    if node[0] == required:
        return node
    frontier = [node]
    explored = set()
    while frontier:
        node = frontier.pop(0)
        explored.add((collapse(node[0]), node[1]))
        for toggle in toggles:
            child = node
            nums = toggle.split(",")
            new_state = list(child[0])
            for num in nums:
                num = int(num.replace("(", "").replace(")",""))
                new_state[num] = "." if new_state[num] == "#" else "#"
            child = (new_state, child[1]+1)
            if (collapse(child[0]), child[1]) not in explored and child not in frontier:
                if child[0] == required:
                    return child
                frontier.append(child)


total = 0
for line in data:
    split_line = line.split()
    state = list(split_line[0][1:-1])
    current = ""
    for i in range(len(state)):
        current += "."
    toggles = split_line[1:-1]
    required = split_line[-1]
    required_ints = []
    for i in required:
        if i.isdigit():
            required_ints.append(int(i))
    solution = bfs((current, 0), toggles, state)
    total += solution[1]
print(total)
