import turtle
wn = turtle.Screen()

pirate = turtle.Turtle()

angle = 0
for x in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(x)
    pirate.forward(100)
    angle = angle + x

print(angle % 360)

wn.mainloop()