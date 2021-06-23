from turtle import Turtle, xcor
import random

class Ball(Turtle):
    """
    Class for the pong ball
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(.5, .5)
        self.color('white')
        self.ball_speed = 10
        self.move_speed = .1
        self.y_move = self.ball_speed
        self.x_move = self.ball_speed

    def reset_ball(self):
        """
        Reset ball to center
        """
        self.goto(0, 0)
        self.move_speed = 0.1

    def move_ball(self):
        """
        Move the ball
        """
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        """
        Given the ball is an object
        Bounce it away at an angle
        """
        self.y_move *= -1

    def paddle_hit(self):
        """
        Given the ball is a the paddle
        Bounce away from it
        """
        self.move_speed *= 0.9
        self.x_move *= -1

    def at_wall(self):
        """
        Given a balls position
        Detemine if it is at a bouncable wall
        Return True
        """
        if self.ycor() == 290 or self.ycor() == -290:
            return True

    def at_paddle(self, paddle):
        """
        Given a balls position
        Determine if it is at the paddle
        Return True
        """
        if self.distance(paddle) < 55:
            if self.xcor() > 350 or self.xcor() < -350:
                return True

    def scored(self):
        """
        Given a ball's location
        Determine if it is past the paddle
        """
        if self.xcor() > 360 or self.xcor() < -360:
            return True
