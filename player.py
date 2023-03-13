STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_pos()
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        if self.ycor() >FINISH_LINE_Y:
            return True

    def reset_pos(self):
        self.goto(STARTING_POSITION)
