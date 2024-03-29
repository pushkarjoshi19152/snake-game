import time
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        random.seed(time.time())


        self.penup()
        self.color('red')
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):

        self.goto(random.randint(-280, 280), random.randint(-280, 280))
