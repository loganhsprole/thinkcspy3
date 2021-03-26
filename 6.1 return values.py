biggest = max(3, 7, 2, 5)
x = abs(3 - 11) + 10
print(biggest)
print(x)


def area(radius):
    return 3.14159 * radius * radius


print(area(2))


def absolute_value(x):
    if x < 0:
        return -x
    return x


print(absolute_value(-2))


def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x


print(bad_absolute_value(0))


def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""


print(find_first_2_letter_word(["this", "is", "a", "dead", "parrot"]))