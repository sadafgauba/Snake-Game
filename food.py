from turtle import Turtle
import random
from screen_setup import ScreenSetup

FOOD_SIZE = 1
FOOD_COLOR = "blue"
FOOD_SHAPE = "circle"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(FOOD_SIZE)
        self.speed(100)

    def show_food(self):
        self.hideturtle()
        self.goto(random.choice([i for i in range(int(-(ScreenSetup().screen_width/2) + 20),
                                                  int(ScreenSetup().screen_width/2), 20)]),
                  random.choice([i for i in range(int(-(ScreenSetup().screen_height/2) + 20),
                                                  int(ScreenSetup().screen_height/2), 20)]))
        self.showturtle()
        return self.pos()
