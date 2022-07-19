from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

for sides in range(3, 11):
    for _ in range(sides):
        timmy.fd(50)
        timmy.left(360/sides)


screen.exitonclick()