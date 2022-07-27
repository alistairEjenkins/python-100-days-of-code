import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Squishy Squirtle")
screen.bgpic('road.gif')
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect reached other side
    if player.reached_finish():
        print("reached finish line")
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    car_manager.car_off_screen()

screen.exitonclick()