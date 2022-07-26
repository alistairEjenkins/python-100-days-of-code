from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, key='p')
screen.onkey(r_paddle.down, key="l")
screen.onkey(l_paddle.up, key='q')
screen.onkey(l_paddle.down, key="a")

playing = True
while playing:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
        

    # detect out of bounds
    # point to right
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

    # point to left
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
        






screen.exitonclick()