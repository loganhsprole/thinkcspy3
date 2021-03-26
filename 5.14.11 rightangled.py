def is_rightangled(a, b, c):
	v = abs((c ** 2) - ((a ** 2) + (b ** 2)))
	print(v < 0.000001)


is_rightangled(3, 4, 6)
