from turtle import Turtle


class Player(Turtle):
    """
    Class for managing a turtle
    """
    def __init__(self):
        super().__init__(shape='turtle')
        self.color('darkgreen')
        self.penup()
        self.setheading(90)
        self.starting_position = (0, -280)
        self.move_speed = 10
        self.finish_line = 280
        self.goto(self.starting_position)

    def move_turtle(self):
        """
        Respond to player controls
        """
        self.forward(self.move_speed)

    def complete_level(self):
        """
        Check if a player has completed the level
        Return True
        """
        if self.ycor() == self.finish_line:
            return True

    def refresh(self):
        """
        Refresh the turtle to the start of the level
        """
        self.goto(self.starting_position)
