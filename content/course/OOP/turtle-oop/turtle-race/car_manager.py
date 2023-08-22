from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
GENERATION_SPEED = [1,3]
RANDOM_COORDINATES = []
 
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_generate = [1,6]
             
    def generate_car(self):
        random_chance = rd.randint(a=self.car_generate[0],b=self.car_generate[1])
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(0.5,1)
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            new_car.goto(280,rd.randint(-280,280))
            self.all_cars.append(new_car)
        
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
    def increase_speed(self):
        self.car_generate = GENERATION_SPEED