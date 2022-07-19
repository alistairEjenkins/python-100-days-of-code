# Hurst dots
import colorgram
from turtle import Turtle, Screen
from random import choice

def get_color(color):

    return int(color.rgb[0]), int(color.rgb[1]), int(color.rgb[2])


screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.title("Dots Picture")

tim = Turtle()
tim.ht()
tim.penup()
y_cor = -200

colors = colorgram.extract("dots.jpg", 9)

for _ in range(16):
    tim.goto(-200, y_cor)
    for _ in range(16):
        tim.pendown()
        tim.dot(10, get_color(choice(colors)))
        tim.penup()
        tim.fd(25)
    y_cor += 25

screen.exitonclick()

