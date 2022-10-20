import turtle
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
SCOREBOARD_COLOR = 'white'


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.scorepen = Turtle()
        self.scorepen.hideturtle()
        self.scorepen.penup()
        self.scorepen.color(SCOREBOARD_COLOR)
        self.highscore = self.fetch_high_score()

    def update_score(self):
        self.score += 1

    def fetch_high_score(self):
        try:
            f = open("highscore.txt", "r")
            v = f.read()
            f.close()
            return int(v)
        except:
            return 0

    def save_new_high_score(self, new_score):
        try:
            f = open("highscore.txt", "r")
            old_score = int(f.read())
            if old_score < int(new_score):
                f.close()
                fw = open("highscore.txt", "w")
                fw.write(new_score)
                fw.close()
                print("New Score Added!")
        except Exception as e:
            print(e)
            f = open("highscore.txt", "w")
            f.write(new_score)
            f.close()

    def display_score(self):
        self.scorepen.clear()
        self.scorepen.goto(0, 270)
        prompt = f"High Score: {self.highscore}, Score: {self.score}"
        self.scorepen.write(prompt, align=ALIGNMENT, font=FONT)

    def display_gameover(self):
        self.scorepen.clear()
        self.scorepen.goto(0, 270)
        prompt = f"Game Over! Final Score: {self.score}"
        self.scorepen.write(prompt, align=ALIGNMENT, font=FONT)
        self.save_new_high_score(str(self.score))
