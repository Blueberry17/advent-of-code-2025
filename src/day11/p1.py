import networkx as nx

data = open("input.txt").read().split("\n")

DG = nx.DiGraph()
for line in data:
    line = line.split()
    current = line[0][:-1]
    for out in line[1:]:
        DG.add_edge(current, out)

print(len(list(nx.all_simple_paths(DG, "you", "out"))))

