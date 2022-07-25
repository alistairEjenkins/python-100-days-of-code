# etch-a-sketch

from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def up():
    tim.fd(10)
    
def down():
    tim.fd(10)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.exitonclick()