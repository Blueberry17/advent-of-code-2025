from functools import lru_cache

@lru_cache(maxsize=None)
def reachable(current, dac, fft):
    if current == "out":
        return dac and fft

    new_dac = dac or (current == "dac")
    new_fft = fft or (current == "fft")

    total = 0
    for nxt in graph[current]:
        total += reachable(nxt, new_dac, new_fft)

    return total

data = open("input.txt").read().splitlines()

graph = {}
for line in data:
    line = line.split()
    current = line[0][:-1]
    graph[current] = line[1:]

print(reachable("svr", False, False))
