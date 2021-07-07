from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

def wager():
    """
    Prompt for a color to be chosen
    Return that color
    """
    bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color')
    return bet

def race(bet):
    """
    Given a players bet
    Run a race and print out if the turtle of the same color as the player's won
    """
    config = {
        'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'purple'],
        'y_axis': [-125, -75, -25, 25, 75, 125]
    }

    turtles = []

    for _ in range(len(config['colors'])):
        racing_turle = Turtle(shape='turtle')
        racing_turle.color(config['colors'][_])
        racing_turle.penup()
        racing_turle.goto(-240, config['y_axis'][_])
        turtles.append(racing_turle)

    lets_race = True

    while lets_race:
        
        for my_turtle in turtles:
            if my_turtle.xcor() > 230:
                lets_race = False
                winning_turtle = my_turtle.pencolor()
                if winning_turtle == bet:
                    print(f'You won! The {winning_turtle} turtle is the winner!')
                else:
                    print(f'You lost! The {winning_turtle} turtle is the winner!')
            dist = random.randint(0, 10)
            my_turtle.forward(dist)


    screen.exitonclick()
