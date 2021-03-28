# Exercise 1. Compass points.


def turn_clockwise(point):
    """Takes a compass point as its parameters and returns the next compass point in the clockwise direction."""
    if point == "N":
        return "E"
    elif point == "E":
        return "S"
    elif point == "S":
        return "W"
    elif point == "W":
        return "N"
    else:
        return None


assert turn_clockwise("N") == "E"
assert turn_clockwise("W") == "N"
assert turn_clockwise(42) == None
assert turn_clockwise("rubbish") == None

# Exercise 2. Convert integer number 0 to 6 into name of a day.


def day_name(day_num):
    """Converts an integer number 0 to 6 into the name of a day."""
    if day_num == 0:
        return "Sunday"
    elif day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    else:
        return None


assert day_name(3) == "Wednesday"
assert day_name(6) == "Saturday"
assert day_name(42) == None