from turtle import Turtle, Screen
import random as rd

screen = Screen()
timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")
timmy.speed("fastest")
timmy.pensize(10)


directions = [90,180,270,360]

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = f"#{r:02X}{g:02X}{b:02X}"
    return random_color

for _ in range(5000):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(rd.choice(directions))
    
screen.exitonclick()