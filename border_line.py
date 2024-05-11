from turtle import Turtle

class BorderLine:
    def __init__(self):
        self.make_border()

    def make_border(self):
        new_border = Turtle()
        new_border.hideturtle()
        new_border.penup()
        new_border.goto(0,240)
        new_border.right(90)
        new_border.pensize(10)
        for x in range(10):
            new_border.pendown()
            new_border.forward(25)
            new_border.penup()
            new_border.forward(25)