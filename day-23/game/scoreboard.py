from turtle import Turtle

class Scoreboard(Turtle):
    """
    Class for keeping score
    And other administrative functions
    """
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(-280, 250)
        self.font = 'Courier'
        self.font_size = 16
        self.font_style = 'normal'
        self.score()

    def score(self):
        self.write(f'Level: {self.level}', align='left', font=(self.font, self.font_size, self.font_style))

    def update_level(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=(self.font, self.font_size, self.font_style))
