from turtle import Turtle


def write_state(state, x, y):
    """
    Given a state name, X and Y coordinate
    Move there and write the state name
    """
    pen = Turtle(visible=False)
    pen.speed('fastest')
    pen.penup()
    pen.goto(x, y)
    pen.write(state)
