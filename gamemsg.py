from turtle import Turtle

class GameMsg(Turtle,):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.welcome_msg()

    def welcome_msg(self):
        self.write("Welcome to the pong game!,who reach to 20 win", False, "center", ("Arial", 30, "normal"))
    def game_over_msg(self,player):
        self.write(f"Player {player} win the game !!", False, "center",("Arial" , 50, "normal") )