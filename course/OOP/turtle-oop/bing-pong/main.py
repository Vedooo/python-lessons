# ball(collasion wall, collasion players )
# paddle(pve & pvp)
# score(collasion with missing ball, keep score)

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time as t

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = Score()
screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("bing-pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    t.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collasion for paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
            
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point() 
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.r_point == 5 or score.l_point == 5:
        score.game_over()
        game_is_on = False
        


screen.exitonclick()