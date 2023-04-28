from turtle import Screen, Turtle
import random
COLORS = ["red", "orange", "yellow", "white", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LEFT = 180
# Car dimensions
CAR_LEN = 2
CAR_WID = 1


class Car(Turtle):
    """Base class that a car will generate as"""
    
    
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.penup()
        self.goto(500, 0) # Off screen
        self.color(random.choice(COLORS))
        self.resizemode("user")
        self.setheading(LEFT)
        self.shapesize(stretch_len=CAR_LEN, stretch_wid=CAR_WID)
        self.screen.update()

class CarManager(Turtle):
    """Player controller paddle for the Pong game"""


    def __init__(self):
        """Snake starting position"""
        super().__init__()
        self.screen = Screen()
        self.car_list = []
        self.spawn_rate = 5
        
    
    def generate_car(self):
        """Generates a car in a random y-cord"""
        
        if random.randint(1, self.spawn_rate) == 1:
            new_car = Car()
            new_car.goto(300 - STARTING_MOVE_DISTANCE, random.randint(-230, 240))
            self.car_list.append(new_car)
        
        
    def move(self, speed):
        """Moves the cars forward"""
        for car in self.car_list:
            car.forward(speed)
            
            
    def increase_spawn_rate(self):
        """Once levels reach higher levels, increase spawn rate of cars slightly"""
        self.spawn_rate -= 1