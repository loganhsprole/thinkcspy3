P = 10000
n = 12
r = 0.08
t = float(input("Years to compound: "))
A = P * (1 + (r / n)) ** (n * t)
print("$", A)
