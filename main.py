import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
turtle = Player()
car_spawn_counter = 0
SPAWN_FREQUENCY = 6
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_spawn_counter += 1
    if car_spawn_counter % SPAWN_FREQUENCY == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move_forward()
        if turtle.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.next_level():
        for car in cars:
            car.increment_distance()
    turtle.next_level()




    screen.listen()
    screen.onkey(turtle.go_up, "Up")

screen.exitonclick()