import turtle
import colorsys

turtle.bgcolor("black")
turtle.pensize(3)
turtle.tracer(5)
turtle.setpos(-90, 80)
turtle.hideturtle()

h = 0.0

for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    turtle.pencolor(c)
    turtle.fd(200)
    turtle.rt(91)
    turtle.circle(60)
    h += 0.009

turtle.done()
