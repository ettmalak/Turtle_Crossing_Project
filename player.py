from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -270)
        self.move_distance = MOVE_DISTANCE

    def next_level(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(0, -270)


    def go_up(self):
        self.forward(MOVE_DISTANCE)





