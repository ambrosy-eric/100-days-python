import random
from turtle import Turtle

class CarManager(Turtle):
    """
    Class for managing Cars on the game board
    """
    def __init__(self):
        self.cars = []
        self.move_distance = 5
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.valid_ycors = list(range(-250, 251, 40))
        
    def generate_car(self):
        """
        Generate car at valid y coordinates
        """
        chance = random.randint(0, 5)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color((random.choice(self.colors)))
            new_car.goto(300, random.choice(self.valid_ycors))
            self.cars.append(new_car)

    def car_move(self):
        """
        Move the car
        """
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        """
        Increase the speed of movement
        """
        self.move_distance += 2.5

    def detect_collision(self, player):
        """
        Given a player's turtle position
        Determine if a car and turtle have collided
        Return True if they have
        """
        for car in self.cars:
            if car.distance(player) < 20:
                return True
