#e2.2DrawPython.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("violet")
turtle.seth(-40)
for i in range(1):
    turtle.circle(40,80)
    turtle.circle(-40,80)
    turtle.pencolor("yellow")
for i in range(1):
    turtle.circle(40,80)
    turtle.circle(-40,80)
    turtle.pencolor("blue")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()