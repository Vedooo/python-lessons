from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 0
        self.lives = 3
        self.update_dashboards()
        self.hideturtle()
        
    def update_dashboards(self):
        self.clear()
        self.goto(300,300)
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.goto(-300,300)
        self.write(f"Live: {self.lives}", align="center", font=FONT)
    
    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_dashboards()
    
    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.update_dashboards()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", move=False, align="center", font = FONT)
    
    