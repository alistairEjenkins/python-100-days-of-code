from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
lanes = [y for y in range(-250,275,25)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        color = choice(COLORS)
        self.color(color)
        self.penup()
        self.hideturtle()
        #starting_y = randint(-250,250)
        self.goto(300, choice(lanes))
        self.showturtle()
        self.speed = STARTING_MOVE_DISTANCE



class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):

        if randint(1,6) == 6:
            self.all_cars.append(Car())

    def move_cars(self):

        for car in self.all_cars:
            car.backward(car.speed)

    def level_up(self):

        for car in self.all_cars:
            car.speed += MOVE_INCREMENT

    def car_off_screen(self):

        for car in self.all_cars[:]:
            if car.xcor() < -330:
                self.all_cars.remove(car)

