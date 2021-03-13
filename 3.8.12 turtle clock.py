import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

clock = turtle.Turtle()
clock.color("blue")
clock.shape("turtle")
clock.pensize(3)

for i in range(12):
    clock.penup()
    clock.forward(140)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(20)
    clock.stamp()
    clock.backward(170)
    clock.left(30)

clock.stamp()

wn.mainloop()
