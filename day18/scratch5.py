from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()

DEGREES = 360
CIRCLES = 20
tilt = DEGREES // CIRCLES
for _ in range(DEGREES // tilt):
    tim.circle(100)
    tim.left(DEGREES // CIRCLES)