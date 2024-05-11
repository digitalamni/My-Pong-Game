import time
from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5,3)
        self.is_on = True
        self.steps = 0


    def move(self):
        self.forward(10)
        self.steps += 0.5
        if self.steps % 10 == 0:
            self.left(90)










