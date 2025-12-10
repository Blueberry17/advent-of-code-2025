data = open("input.txt").read().split()

points = []
for point in data:
    x, y = point.split(",")
    points.append((int(x), int(y)))

maximum = 0
for x1, y1 in points:
    for x2, y2 in points:
        space = (1+abs(x1-x2)) * (1+abs(y1-y2))
        if space > maximum:
            maximum = space
            max_points = [(x1, y1), (x2, y2)]

print(maximum)
