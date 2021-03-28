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


# Exercise 3: Convert name of a day into integer number 0 to 6.


def day_num(day_name):
    """Converts the name of a day into an integer number 0 to 6."""
    if day_name == "Sunday":
        return 0
    elif day_name == "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == "Saturday":
        return 6
    else:
        return None


assert day_num("Friday") == 5
assert day_num("Sunday") == 0
assert day_num(day_name(3)) == 3
assert day_name(day_num("Thursday")) == "Thursday"
assert day_num("Halloween") == None


# Exercise 4. Answer questions like "Today is Wednesday. I leave on holiday in 19 days time. What day will that be?"


def day_add(day, delta):
    """Takes a day name and a delta argument and returns a resulting day name."""
    return day_name((day_num(day) + delta) % 7)


assert day_add("Monday", 4) == "Friday"
assert day_add("Tuesday", 0) == "Tuesday"
assert day_add("Tuesday", 14) == "Tuesday"
assert day_add("Sunday", 100) == "Tuesday"


# Exercise 5. Does day_add work with negative deltas?


assert day_add("Sunday", -1) == "Saturday"
assert day_add("Sunday", -7) == "Sunday"
assert day_add("Tuesday", -100) == "Sunday"
