FONT = ("Courier", 24, "normal")
from turtle import Turtle,Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):

        self.write(f"Level: {self.level} ", align= "center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over ", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()