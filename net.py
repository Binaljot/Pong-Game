from turtle import Turtle


class Net(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.5)  # Making the 20 by 20 paddle to 20 by 10
        self.penup()
        self.goto(position)
