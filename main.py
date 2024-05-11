# IMPORTS

from turtle import Screen
from paddle import Paddle
from ball import Ball
from border_line import BorderLine
from score import Score
from bounus_turtle import BounusTurtle
from snake import Snake
from gamemsg import GameMsg
import headings
import time

#INIT

SCORE_LOC_R = (100, 180)
SCORE_LOC_L = (-100, 180)
screen = Screen()
screen.setup(1000, 500)
msg = GameMsg()
msg.welcome_msg()
time.sleep(2)
msg.clear()

screen.listen()
paddels = Paddle()
border = BorderLine()
score_l = Score(SCORE_LOC_L, "LEFT")
score_r = Score(SCORE_LOC_R, "RIGHT")
screen.tracer(0)
bounus_turtle1 = BounusTurtle()
bounus_turtle1.hideturtle()
snake = Snake()
snake.goto(-100, -100)
snake.hideturtle()

snake_is_on = True

ball = Ball()
ball.refrash(0, 360)


#FUNCTIONS
def cheacking_bouns(obj, score_l, score_r, points):
    if ball.check_heading():
        score_l.update(points)
        obj.hideturtle()
        obj.is_on = False

    else:
        score_r.update(points)
        obj.hideturtle()
        obj.is_on = False


#LISTEN KEYS
screen.onkey(paddels.move_left_up, "e")
screen.onkey(paddels.move_left_down, "d")
screen.onkey(paddels.move_right_up, "Up")
screen.onkey(paddels.move_right_down, "Down")

# THE GAME
is_true = True
while is_true:

    time.sleep(0.05)
    screen.update()
    ball.move()

    # BOUNCING BALL RULES
    if ball.ycor() < -250.0:
        ball.wall_bounce(headings.NORTH_EAST, headings.NORTH_WEST)

    if ball.ycor() > 250.0:
        ball.wall_bounce(headings.SOUTH_EAST, headings.SOUTH_WEST)

    if ball.xcor() < -430 and ball.distance(paddels.paddle_l[2]) < 50:
        ball.bounce(headings.SOUTH_EAST, headings.EXTRA_EAST_SOUTH, headings.EAST, headings.EXTRA_EAST_NORTH,
                    headings.NORTH_EAST, paddels.paddle_l)

    if ball.xcor() > 430 and ball.distance(paddels.paddle_r[2]) < 50:
        ball.bounce(headings.SOUTH_WEST, headings.EXTRA_WEST_SOUTH, headings.WEST, headings.EXTRA_WEST_NORTH,
                    headings.NORTH_WEST, paddels.paddle_r)

    # BALL GOALS
    if ball.xcor() < -520:
        score_r.update(1)
        time.sleep(0.5)
        ball.speed += 0.5
        ball.refrash(headings.NORTH, headings.SOUTH)

    if ball.xcor() > 520:
        score_l.update(1)
        time.sleep(0.5)
        ball.speed += 0.5
        ball.refrash(headings.SOUTH, headings.TOTAL_NORTH)

    # BONUS TURTEL STAGE
    if score_l.score > 2 or score_r.score > 2:
        if bounus_turtle1.is_on == True:
            bounus_turtle1.showturtle()

            if ball.distance(bounus_turtle1) < 50:
                if bounus_turtle1.is_on == True:
                    cheacking_bouns(bounus_turtle1, score_l, score_r, 3)
    # BONUS SNAKE STAGE
    if score_l.score > 6 and bounus_turtle1.is_on == False or score_r.score > 6 and bounus_turtle1.is_on == False:
        if snake.is_on:
            snake.showturtle()
            snake.move()

            if ball.distance(snake) < 30:
                if snake.is_on == True:
                    cheacking_bouns(snake, score_l, score_r, 20)
                    if snake.is_on == False:
                        is_true = False
    # SCORE LIMIT
    if score_l.score >= 20 or score_r.score >= 20:
        is_true = False

# FINAL MSG
screen.clear()
if score_l.score > score_r.score:
    msg.game_over_msg(score_l.name)
else:
    msg.game_over_msg(score_r.name)

screen.exitonclick()
