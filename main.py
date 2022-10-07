import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Cross the Road")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
