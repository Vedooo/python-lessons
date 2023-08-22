from colors import rgb_colors
from turtle import Turtle, Screen, colormode
import random as rd

screen = Screen()
drawer = Turtle()
colormode(255)

drawer.shape("arrow")
drawer.speed("fastest")
drawer.penup()
drawer.hideturtle()
drawer.setheading(225)
drawer.forward(400)
drawer.setheading(0)

num_dots = 100


for _ in range(1, num_dots + 1):
    drawer.dot(20, rd.choice(rgb_colors))
    drawer.forward(50)

    if _ % 10 == 0:
        drawer.setheading(90)
        drawer.forward(50)
        drawer.setheading(180)
        drawer.forward(500)
        drawer.setheading(0)


drawer.screen().exitonclick()





screen.exitonclick()