from turtle import Turtle
FONT = ("Arial" , 50, "normal")
class Score(Turtle):
    def __init__(self,loc,name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(loc)
        self.write_score()
        self.name=name

    def write_score(self):
        self.write(self.score, False, "center",FONT )
    
    def update(self,n1):
        self.score += n1
        self.clear()
        self.write_score()





        
