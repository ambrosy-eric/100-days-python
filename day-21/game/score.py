from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
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
        self.clear()
        self.write(f'Score: {self.score} - High Score: {self.high_score}', align=self.align, font=(self.font, self.font_size, self.font_style))

    def increase_score(self):
        """
        Increase the score by 1
        """
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        """
        At game end
        Determine if new score is greater than high score
        If so, update high score start new game
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./game/data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def get_high_score(self):
        """
        Grab an value from data.txt
        Set it as an int and the highscore
        """
        with open('./game/data.txt', 'r') as file:
            number = file.read()
            self.high_score = int(number)
