from turtle import Turtle, Screen, width
from random import randint
from racer import Racer



screen = Screen()
screen.setup(500, 400)
screen.title('Turtle Racer')

racers = [Racer(num) for num in range(7)]

racing = True
prediction = screen.textinput("Turtle Racer", "Who will win? Pick a color.")
while racing:
    racer_number = randint(0,6)
    chosen_racer = racers[racer_number]
    chosen_racer.move()
    if chosen_racer.xcor() >= 230:
        winner = chosen_racer.turtle_color
        racing = False

if prediction == winner:
    screen.textinput("Congrats!", f"You choose the winning turtle {winner}")
else:
    screen.textinput("Unlucky", f"{winner} won instead ")
screen.exitonclick()