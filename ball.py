from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed = 20

    def move(self):
        self.forward(self.speed)


    def refrash(self,n1,n2):
        self.goto(0,0)
        self.setheading(random.randint(n1,n2))

    def bounce(self,n1,n2,n3,n4,n5,paddle):
        if self.distance(paddle[0]) < 15:
            self.setheading(n1)
        elif self.distance(paddle[1]) < 15:
            self.setheading(n2)
        elif self.distance(paddle[2]) < 15:
            self.setheading(n3)
        elif self.distance(paddle[3]) < 15:
            self.setheading(n4)
        elif self.distance(paddle[4]) < 15:
            self.setheading(n5)

    def check_heading(self):
        if self.heading() >= 0 and self.heading() <= 90 or self.heading() >= 270 and self.heading() <= 360:
            return True
        elif self.heading() > 90 and self.heading() < 270:
            return False

    def wall_bounce(self,h1,h2):
        if self.check_heading() == True:
            self.setheading(h1)
        elif self.check_heading() == False:
            self.setheading(h2)


