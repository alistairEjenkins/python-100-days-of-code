from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reached_finish(self):
        return self.ycor() == FINISH_LINE_Y

