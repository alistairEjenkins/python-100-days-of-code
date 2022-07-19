from turtle import Turtle, Screen
screen = Screen()

timmy = Turtle()
timmy.penup()
timmy.goto(-200,0)
for _ in range(10):
    timmy.fd(20)
    timmy.penup()
    timmy.fd(20)
    timmy.pendown()
screen.exitonclick()


