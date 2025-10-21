from ast import increment_lineno
from random import randint
from turtle import Turtle
from player import Player
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.rand_y= randint(-250, 270)
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_forward()
        self.create_Turtle()


    def create_Turtle(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, self.rand_y)
        self.move_forward()

    def move_forward(self):
        self.backward(self.move_distance)

    def increment_distance(self):
        self.move_distance += MOVE_INCREMENT

