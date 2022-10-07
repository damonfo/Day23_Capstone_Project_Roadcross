from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.goto(-220, 250)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def update_point(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
