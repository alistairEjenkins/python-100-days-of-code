import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')


guessed_states = []
while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{len(guessed_states)}/50 States found", "What is the name of the next state?").capitalize()

    if answer_state == "Exit":
        missing_states = [state for state in data.state.to_list() if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states-to-learn.csv')
        break
    if answer_state in data.state.to_list():
        t = Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(state.state.item())
        guessed_states.append(answer_state)




