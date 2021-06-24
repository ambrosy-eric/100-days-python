import time
from turtle import Screen
from game.player import Player
from game.cars import CarManager
from game.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()

screen.onkey(player.move_turtle, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_car()
    car.car_move()

    if car.detect_collision(player.pos()):
        game_is_on = False
        score.game_over()

    if player.complete_level():
        player.refresh()
        car.increase_speed()
        score.update_level()


screen.exitonclick()
