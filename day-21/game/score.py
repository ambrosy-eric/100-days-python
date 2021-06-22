from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.shape()
        self.hideturtle()
        self.sety(280)
        self.align = 'center'
        self.font = 'Geneva'
        self.font_size = 10
        self.font_style = 'bold'
        self.update_score()

    def update_score(self):
        """
        Update the score
        """
        self.write(f'Score: {self.score}', align=self.align, font=(self.font, self.font_size, self.font_style))

    def increase_score(self):
        """
        Increase the score by 1
        """
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self.align, font=(self.font, 20, self.font_style))