import time
from turtle import Screen, Turtle
from game.pong import Pong
from game.ball import Ball
from game.scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    # screen.tracer(0)

    paddle1 = Pong((360, 0))
    paddle2 = Pong((-360, 0))
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    
    screen.onkey(paddle1.paddle_up, 'Up')
    screen.onkey(paddle1.paddle_down, 'Down')
    screen.onkey(paddle2.paddle_up, 'w')
    screen.onkey(paddle2.paddle_down, 's')

    game_on = True
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move_ball()

        if ball.at_wall():
            ball.wall_bounce()

        if ball.at_paddle(paddle1.pos()) or ball.at_paddle(paddle2.pos()):
            ball.paddle_hit()

        if ball.scored():
            if ball.xcor() > 360:
                score.player1_point()
            elif ball.xcor() < -360:
                score.player2_point()
            ball.reset_ball()

        if score.game_over():
            game_on = False

    screen.exitonclick()

if __name__ == '__main__':
    main()
