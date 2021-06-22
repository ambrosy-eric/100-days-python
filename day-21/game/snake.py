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
            position = ((-20 * body), 0)
            self._add_segment(position)

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

    def at_wall(self):
        wall = 295
        if self.head.xcor() > wall:
            return True
        elif self.head.xcor() < -wall:
            return True
        elif self.head.ycor() > wall:
            return True
        elif self.head.ycor() < -wall:
            return True
        else:
            return False

    def _add_segment(self, position):
        """
        Given the position of the snake
        Add a new segment to it
        """
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        """
        Add a new segment to the snake
        """
        self._add_segment(self.snake[-1].position())

    def collision(self):
        """
        Determine if the snake's head is in contact with its body
        Return True
        """
        for body in self.snake[1:]:
            if self.head.distance(body) < 10:
                return True
