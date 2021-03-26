biggest = max(3, 7, 2, 5)
x = abs(3 - 11) + 10
print(biggest)
print(x)


def area(radius):
    return 3.14159 * radius * radius


a = area(2)
print(a)


def absolute_value(x):
    if x < 0:
        return -x
    return x


b = absolute_value(-2)
print(b)