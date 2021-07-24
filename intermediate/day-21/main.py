import time
from turtle import Screen
from game.snake import Snake
from game.food import Food
from game.score import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_on = True
    while game_on:
        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        if snake.at_wall():
            score.reset_score()
            snake.reset_snake()

        if snake.collision():
            score.reset_score()
            snake.reset_snake()

    screen.exitonclick()

if __name__ == '__main__':
    main()
