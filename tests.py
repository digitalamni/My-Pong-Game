from turtle import Turtle , Screen
from paddle import Paddle
from snake import Snake
left = -1
distanse = 50
# tomy = Turtle()
screen = Screen()
screen.setup(1000,500)
# screen.tracer(0)

snake = Snake()
snake.move()

# screen.update()




screen.exitonclick()
