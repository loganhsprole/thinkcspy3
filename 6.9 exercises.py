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
		return


assert turn_clockwise("N") == "E"
assert turn_clockwise("W") == "N"
assert turn_clockwise(42) == None
assert turn_clockwise("rubbish") == None