import turtle
wn = turtle.Screen()

poly = turtle.Turtle()

for tri in range(3):
    poly.left(360 / 3)
    poly.forward(90)

for tri in range(4):
    poly.left(360 / 4)
    poly.forward(90)

for tri in range(6):
    poly.left(360 / 6)
    poly.forward(90)

for tri in range(8):
    poly.left(360 / 8)
    poly.forward(90)

wn.mainloop()
