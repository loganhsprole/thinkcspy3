import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def area(radius):
    return 3.14159 * radius * radius


def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


print(area2(5, 5, 4, 4))
