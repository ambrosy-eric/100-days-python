from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('yellow')
        self.speed('fastest')
        self.goto(self.random_cordinate())
        self.refresh()

    def random_cordinate(self):
        """
        Generates a random cordinate
        Returns a tuple
        """
        cordinate = []
        for _ in range(2):
            cordinate.append(random.randint(-270, 270))
        return tuple(cordinate)

    def refresh(self):
        self.goto(self.random_cordinate())