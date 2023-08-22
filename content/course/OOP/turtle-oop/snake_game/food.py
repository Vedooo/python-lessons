from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        random_x = rd.randint(-280,280)
        random_y = rd.randint(-280,280)
        self.goto(x = random_x, y = random_y)