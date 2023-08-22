from turtle import Turtle, Screen
import random as rd

screen = Screen()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shapes(num_edge_n):
    angle = 360 / num_edge_n
    for _ in range(num_edge_n):
        timmy.forward(100)
        timmy.left(angle)

for i in range(3, 30):
    timmy.color(rd.choice(colors))
    draw_shapes(i)



screen.exitonclick()
