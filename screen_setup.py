from turtle import Screen

BACKGROUND_COLOR = "black"
SCREEN_TITLE = "Snake Game"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class ScreenSetup:

    def __init__(self):
        self.screen = None
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def setup(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title(SCREEN_TITLE)
        self.screen.tracer(0)

        return self.screen
