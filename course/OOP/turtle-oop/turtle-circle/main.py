from turtle import Turtle,Screen
import random as rd

screen = Screen()
timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")
timmy.speed("fastest")

r = 100

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = f"#{r:02X}{g:02X}{b:02X}"
    return random_color

def create_circle():
    timmy.circle(r)
    timmy.left(rd.randint(0,360))

for i in range(1000):
    timmy.color(random_color())
    create_circle()

screen.exitonclick()