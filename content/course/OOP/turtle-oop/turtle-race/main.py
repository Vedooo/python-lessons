import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.go_to_start()
            score.decrease_lives()
            if score.lives == 0:
                score.game_over()
                game_is_on = False
            
        if player.ycor() > 280:
            score.increase_level()
            player.go_to_start()
            car_manager.level_up()
            car_manager.increase_speed()
            
            
            
            
            

screen.exitonclick()