from turtle import Turtle
LOC_RIGHT_TO_LEFT = [(480,-40),(480,-20),(480,0),(480,20),(480,40),(-480,-40),(-480,-20),(-480,0),(-480,20),(-480,40)]
SIDE_UP= 1
SIDE_DOWN = -1
PADDLE_SPEED = 30


class Paddle:
    def __init__(self):
        self.paddle_r = []
        self.paddle_l = []
        self.make_paddles()
        print(self.paddle_r)
        print(self.paddle_l)

    def make_paddles(self):
        for loc in range(0,10):
            new_sagment = Turtle(shape="square")
            new_sagment.penup()
            new_sagment.goto(LOC_RIGHT_TO_LEFT[loc])
            if loc <= 4:
                self.paddle_r.append(new_sagment)
            else:
                self.paddle_l.append(new_sagment)



    def move(self,paddle,side):
        head = paddle[0]
        for x in range(4, 0, -1):
            new_y = paddle[x].ycor() + PADDLE_SPEED * side
            regular_x = paddle[x].xcor()
            paddle[x].goto(regular_x, new_y)
        head.goto(regular_x, head.ycor() + PADDLE_SPEED * side)

    def move_right_up(self):
        self.move(self.paddle_r,SIDE_UP)

    def move_right_down(self):
        self.move(self.paddle_r,SIDE_DOWN)

    def move_left_up(self):
        self.move(self.paddle_l,SIDE_UP)

    def move_left_down(self):
        self.move(self.paddle_l,SIDE_DOWN)
