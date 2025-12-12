from turtle import Turtle
import random

class Food(Turtle):

    def _init_(self):
        super()._init_()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # small size
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # Pick a random x and y position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        