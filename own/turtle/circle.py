import turtle
import colorsys

bgcolor("black")
pensize(3)
tracer(5)
setpos(-90, 80)
hideturtle()

h = 0.0

for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    fd(200)
    rt(91)
    circle(60)
    h += 0.009

done()
