# random walk

from turtle import Turtle, Screen
from random import randint

screen = Screen()
timmy = Turtle()

for _ in range(randint(10,49)):
    timmy.fd(randint(10,20))
    timmy.left(randint(1,360))
screen.exitonclick()