from turtle import Turtle, Screen
import time
from screen_setup import ScreenSetup

SPEED = 10
MOVE_DISTANCE = 20
FILL_COLOR = "white"
PEN_COLOR = "black"
SHAPE = "square"
INITIAL_BODY = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.screen = ScreenSetup().setup()
        self.screen.tracer(0)
        self.head_position = None
        self.extra_space = None
        self.entire_snake = self.create_body()
        self.head = self.entire_snake[0]
        self.body_coordinates = []

    def create_body(self):
        index = 0
        entire_snake = []
        for i in range(INITIAL_BODY):
            snake = self.create_part()
            snake.goto(0 - index, 0)
            index += 20
            entire_snake.append(snake)

        return entire_snake

    def create_part(self):
        snake = Turtle()
        snake.speed(100)
        snake.shape(SHAPE)
        snake.fillcolor(FILL_COLOR)
        snake.pencolor(PEN_COLOR)
        snake.speed(SPEED)
        snake.penup()

        return snake

    def add_part(self, extra_space):
        snake = self.create_part()
        snake.goto(extra_space)
        self.entire_snake.append(snake)

    def move(self):
        new_coordinate = None
        self.body_coordinates = []
        for i in self.entire_snake:
            if i == self.head:
                new_coordinate = i.pos()
                i.forward(MOVE_DISTANCE)
                self.head_position = i.pos()
            else:
                old_coordinate = i.pos()
                i.goto(new_coordinate)
                self.body_coordinates.append(new_coordinate)
                new_coordinate = old_coordinate

        return self.head_position, new_coordinate

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def direction_update(self):
        self.screen.update()
        time.sleep(0.1)
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")

    def detect_collision(self):
        if self.head.xcor() > (int(ScreenSetup().screen_width/2) - 1) \
                or self.head.ycor() > (int(ScreenSetup().screen_height/2) - 1) \
                or self.head.xcor() < (int(-(ScreenSetup().screen_width/2) + 1)) \
                or self.head.ycor() < (int(-(ScreenSetup().screen_height/2) + 1)):
            return True
        for part in self.entire_snake[1:]:
            if self.head.distance(part) < 5:
                return True
        return False

    def click_exit(self):
        self.screen.exitonclick()
