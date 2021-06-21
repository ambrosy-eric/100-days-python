import time
from turtle import Screen
from game.snake import Snake

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()

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

    screen.exitonclick()

if __name__ == '__main__':
    main()
