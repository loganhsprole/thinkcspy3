def is_rightangled(a, b, c):
    if c > a and c > b:
        v = abs((c ** 2) - ((a ** 2) + (b ** 2)))
    elif b > c and b > a:
        v = abs((b ** 2) - ((c ** 2) + (a ** 2)))
    elif a > b and a > c:
        v = abs((a ** 2) - ((b ** 2) + (c ** 2)))

    print(v < 0.000001)


is_rightangled(5, 3, 4)