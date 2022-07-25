from turtle import Turtle
STARTING_Y = -150
LANE_WIDTH = 30

class Racer(Turtle):

    COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    def __init__(self, number) -> None:
        super().__init__()
        self.shape('turtle')
        self.turtle_color = self.COLORS[number]
        self.color(self.turtle_color)
        self.penup()
        self.goto(-230,STARTING_Y + number * LANE_WIDTH)

    def move(self):
        self.fd(10)