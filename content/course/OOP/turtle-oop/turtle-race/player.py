from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.turtlesize(stretch_len=1,stretch_wid=1)
        self.goto(STARTING_POSITION)
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)    
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        