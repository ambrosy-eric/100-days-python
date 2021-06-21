from turtle import Turtle

class Snake():
    """
    Class for managing a snake
    """
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """
        Create a snake body from turtles
        """
        for body in range(3):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto((-20 * body), 0)
            self.snake.append(segment)

    def move(self, dist=20):
        """
        Given a distance to move
        Move the snake that distance
        """
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(dist)   

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
