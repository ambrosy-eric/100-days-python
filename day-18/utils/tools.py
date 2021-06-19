import colorgram
import random
import turtle as t

def generate_rgb(image, colors):
    """
    Given an image and number of colors to extract
    Extract colors from an image
    Return a list of tuples of rgb colors
    """
    color_list = []
    for color in colorgram.extract(image, colors):
        rgb = color.rgb
        color_rgb = []
        for i in rgb:
            color_rgb.append(i)
        color_list.append(tuple(color_rgb))

    return color_list

def make_dots(n, rows, colors):
    """
    Given a number of dots to create and a list of rgb values
    Create dots via turtle
    """
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.penup()
    t.colormode(255)
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    new_x = turtle.position()[0]
    new_y = turtle.position()[0]
    row = 0
    while row < rows:
        for i in range(n):
            turtle.dot(20, random.choice(colors))
            turtle.forward(50)
        print(turtle.position())
        new_y += 50
        turtle.goto(new_x, new_y)
        row += 1
    screen = t.Screen()
    screen.exitonclick()