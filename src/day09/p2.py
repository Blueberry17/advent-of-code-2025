from shapely.geometry.polygon import Polygon

data = open("input.txt").read().split()

points = []
for point in data:
    x, y = point.split(",")
    points.append((int(x), int(y)))

polygon = Polygon(points)

maximum = 0
for x1, y1 in points:
    for x2, y2 in points:
        valid = True
        space = (1+abs(x1-x2)) * (1+abs(y1-y2))
        new_shape = Polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)))
        if polygon.contains(new_shape):
            if space > maximum:
                maximum = space

print(maximum)
