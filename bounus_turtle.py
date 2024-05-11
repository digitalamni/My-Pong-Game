from turtle import Turtle
import random


class BounusTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.shapesize(5)
        self.penup()
        self.goto(self.random_location())
        self.is_on = True
        # self.bouns_is_on()


    def random_location(self):
        new_x = random.randint(-180,180)
        new_y = random.randint(-220,220)
        return(new_x,new_y)


    def hide(self):
        self.hideturtle()
        self.is_on = False

    def show(self):
        self.showturtle()
        self.is_on = True
