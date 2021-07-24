from turtle import Turtle

class Pong(Turtle):
    """
    Class to manage Pong game
    """
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """
        Create a chain of turtles to be a paddle
        """
        self.shape('square')
        self.color('white')
        self.shapesize(1, 5, .1)
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.goto(position)

    def paddle_up(self):
        """
        Move the paddle up
        """
        self.setheading(90)
        self.forward(25)

    def paddle_down(self):
        """
        Move the paddle down
        """
        self.setheading(270)
        self.forward(25)
