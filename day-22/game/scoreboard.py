from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.align = 'center'
        self.font = 'Geneva'
        self.font_size = 20
        self.font_style = 'bold'
        self.speed('fastest')
        self.update_score()

    def update_score(self):
        """
        Update the score
        """
        self.write(f'{self.player1_score} - {self.player2_score}', align=self.align, font=(self.font, self.font_size, self.font_style))

    def player1_point(self):
        """
        Increase the score by 1
        """
        self.player1_score += 1
        self.clear()
        self.update_score()

    def player2_point(self):
        """
        Increase the score by 1
        """
        self.player2_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """
        End game
        """
        if self.player1_score > 21 or self.player2_score > 21:
            winner = ''
            if self.player1_score > self.player2_score:
                winner = 'Player 1'
            else:
                winner = 'Player 2'
            self.goto(0, 0)
            self.write(f'{winner} wins!', align='center', font=(self.font, 40, self.font_style))
            return True
