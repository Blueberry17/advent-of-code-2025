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

G = nx.Graph()
G.add_nodes_from(data)

for _ in range(10000):
    minimum = float("inf")
    for point in data:
        if list(distances[point].values())[0] < minimum:
            minimum = list(distances[point].values())[0]
            min_val = (point, list(distances[point].keys())[0])

    del distances[min_val[0]][min_val[1]]
    del distances[min_val[1]][min_val[0]]

    G.add_edge(min_val[0], min_val[1])
    if nx.is_connected(G):
        break

point1 = min_val[0].split(",")
point2 = min_val[1].split(",")
print(int(point1[0]) * int(point2[0]))
