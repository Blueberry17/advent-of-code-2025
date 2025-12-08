import math
import networkx as nx

data = open("input.txt").read().split()

distances = {}
for point in data:
    distances[point] = {}

for point1 in data:
    (x1, y1, z1) = tuple(map(int, point1.split(",")))
    for point2 in data:
        if point1 == point2:
            continue
        (x2, y2, z2) = tuple(map(int, point2.split(",")))
        distance = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        distances[point1][point2] = distance
    distances[point1] = dict(sorted(distances[point1].items(), key=lambda item: item[1]))

connections = []
for _ in range(1000):
    minimum = float("inf")
    for point in data:
        if list(distances[point].values())[0] < minimum:
            minimum = list(distances[point].values())[0]
            min_val = (point, list(distances[point].keys())[0])
    connections.append(min_val)
    del distances[min_val[0]][min_val[1]]
    del distances[min_val[1]][min_val[0]]

circuits = []
for a, b in connections:
    found = False
    for circuit in circuits:
        if a in circuit:
            circuit.add(b)
            found = True
        if b in circuit:
            circuit.add(a)
            found = True
    if not found:
        circuits.append({a,b})

g = nx.Graph()
for s in circuits:
    if not s:
        continue
    elems = list(s)
    g.add_nodes_from(elems)
    g.add_edges_from((elems[0], x) for x in elems[1:])

circuits = [set(c) for c in nx.connected_components(g)]
lengths = sorted(list(map(len, circuits)))
total = lengths[-1] * lengths[-2] * lengths[-3]
print(total)
